#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Command line interface for Venominator

Author: hnp
Repo: https://github.com/hobnobpirate/venominator
"""

from subprocess import call

import click

from venominator import attributes
from venominator.venom import Venom


def print_options(s: dict) -> None:
    """Prints the contents of a dictionary.

    :param s<dict>: dictionary of options
    """
    for k, v in s.items():
        print(k, v)


def get_input_int(msg: str) -> int:
    """Gets user input and converts to integer

    :param msg<str>: Message to display to user prompting input
    """
    try:
        return int(input(f"{msg}: "))
    except ValueError:
        return get_input_int(msg)


def check_input(s: dict, i: int):
    """Checks to see if user supplied input is in a dictionary

    :param s<dict>: Dictionary with options to check against
    :param i<int>: Integer value to check if it exists as a key in `s`
    """
    if i in s.keys():
        return s[i]
    else:
        return False


def set_attr_from_dict(s: dict, msg: str) -> str:
    """Control function to prompt user, check dictionary, and return string with selection

    :param s<dict>: Dictionary with options
    :param msg<str>: String to prompt user
    :return <str>: User selected option -- value of dictionary based on user input (key)
    """
    if s == None:
        return None
    try:
        print_options(s)
    except Exception as e:
        print(e)
    i = get_input_int(msg)
    if check_input(s, i):
        return check_input(s, i)
    else:
        return set_attr_from_dict(s, msg)


def input_choice(msg: str) -> bool:
    """Prompt for yes/no user response
    
    :param msg: The message to display to the user.
    :return <bool>:
    """
    i = input(f"{msg} (y/n): ").lower()
    if i == "y":
        return True
    elif i == "n":
        return False
    else:
        return input_choice(msg)


def build_config(v: Venom) -> str:
    """Builds final config output for user review

    :param v<Venom object>: Object containing msfvenom attributes
    :return config<string>: Formatted configuration of msfvenom payload based on selections.
    """
    config = "\n\nCONFIGURATION\n"
    if v.arch:
        config += f"Architecture:\t\t{v.arch}\n"
    config += f"Platform:\t\t{v.platform}\n"
    config += f"Payload:\t\t{v.payload}\n"
    if "reverse" in v.payload:
        config += f"Callback IP:\t\t{v.address}\n"
        config += f"Callback Port:\t\t{v.port}\n"
    else:
        config += f"Listening Port:\t\t{v.port}\n"
    if v.encoder:
        config += f"Encoder:\t\t{v.encoder}\n"
        config += f"Iterations:\t\t{v.iterations}\n"
    config += f"Format:\t\t\t{v.format}\n"
    if v.badchars:
        config += f"Bad characters:\t\t{v.badchars}\n"
    config += f"Output file:\t\t{v.outfile}\n"
    if v.additional:
        config += f"Additional options:\t{v.additional}\n"
    config += f"Build command:\t\t{v.cmd}\n"
    return config


def build_payload(venom: Venom) -> None:
    """Runs msfvenom with user selected options"""
    try:
        call(venom.cmd, shell=True)
        filename = venom.outfile
        with open(filename + ".meta", "w") as f:
            f.write(build_config(venom))
    except FileNotFoundError:
        print("Looks like you don't have msfvenom installed in your PATH")


@click.command()
def cli() -> None:
    """Command line interface for Venominator
    
    Controls the flow of creating msfvenom based payloads.
    Entry point for venominator
    """
    print_banner()
    v = Venom()

    v.platform = set_attr_from_dict(attributes.list_platforms(), "Select platform")

    v.arch = set_attr_from_dict(
        attributes.list_arches(v.platform), "Select architecture"
    )

    v.payload = set_attr_from_dict(
        attributes.filter_payloads(v.platform, v.arch), "Select payload"
    )

    if "reverse" in v.payload:
        v.port = get_input_int("Enter port to call back to")
        v.address = input("Enter IP address/interface to call back to: ")
    else:
        v.port = get_input_int("Enter port to listen on")

    try:
        if attributes.list_encoders(v.arch):
            if input_choice("Would you like to encode the payload?"):
                v.encoder = set_attr_from_dict(
                    attributes.list_encoders(v.arch), "Select encoder"
                )
    except TypeError:
        pass

    if v.encoder:
        v.iterations = get_input_int("Enter number of iterations")

    v.format = set_attr_from_dict(attributes.list_formats(), "Select output format")

    if v.format not in attributes.ex_formats and input_choice(
        "Any bad characters to avoid?"
    ):
        v.badchars = input("Enter bad characters in quotes: ")

    v.outfile = input("Enter output filename: ")

    if input_choice("Would you like to add additional options?"):
        v.additional = input("Enter additional options: ")

    v.build_cmd()
    print(build_config(v))
    if input_choice("Would you like to run the command?"):
        build_payload(v)


def print_banner() -> None:
    """Because ASCII art is fun."""
    banner = """
     _    __                           _             __            
    | |  / /__  ____  ____  ____ ___  (_)___  ____ _/ /_____  _____
    | | / / _ \/ __ \/ __ \/ __ `__ \/ / __ \/ __ `/ __/ __ \/ ___/
    | |/ /  __/ / / / /_/ / / / / / / / / / / /_/ / /_/ /_/ / /    
    |___/\___/_/ /_/\____/_/ /_/ /_/_/_/ /_/\__,_/\__/\____/_/     
    """
    print(banner)


if __name__ == "__main__":
    cli()
