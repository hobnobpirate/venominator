#!/usr/bin/python3

from os import system


# The following files must be in the same directory as this script:
# archs.txt encoders.txt formats.txt payloads.txt platforms.txt


class Venom(object):
    def __init__(self):
        self.d = {}

    def set_opt(self, opt_name: str, switch: str, user: bool = False, src: str = None):
        opt = get_opt(opt_name, user, src)
        if opt:
            if switch == "LHOST=" or switch == "LPORT=":
                opt_value = f"{switch}{opt}"
            else:
                opt_value = f"{switch} {opt}"
            self.d.update({opt_name: opt_value})

    def build_cmd(self) -> str:
        self.base = "msfvenom "  # need trailing space here for command
        options = []
        for v in self.d.values():
            options.append(v)
        self.cmd = self.base + " ".join(options)
        return self.cmd


def get_opt(opt_name: str, user: bool, src: str) -> str:
    system("clear")
    if user:
        return get_user_input(opt_name)
    if src:
        options = list_opts(src)
        print(f"Available {opt_name}s:")
        for x, y in options.items():
            print(f"{x}\t{y}")
        try:
            select = int(input(f"Select {opt_name}: "))
        except ValueError:
            return None
        if select in options.keys():
            return options[select]
        else:
            get_opt(opt_name, user, src)


def get_user_input(opt_name: str) -> str:
    user_input = input(f"Enter {opt_name}: ")
    if user_input == "":
        pass
    else:
        return user_input


def list_opts(src: str) -> dict:
    with open(src, "r") as f:
        options = f.readlines()
        c = 1
        d = {}
        for option in options:
            d.update({c: option.strip()})
            c += 1
    return d


if __name__ == "__main__":
    # d = {"key": ("prompt", "cmd line switch", UserInteraction, "Source File")}
    d = {
        "arch": ("architecture", "-a", False, "archs.txt"),
        "platform": ("platform", "--platform", False, "platforms.txt"),
        "format": ("format", "-f", False, "formats.txt"),
        "payload": ("payload", "-p", False, "payloads.txt"),
        "lhost": ("LHOST", "LHOST=", True),
        "lport": ("LPORT", "LPORT=", True),
        "badchars": ("bad characters (include quotes)", "-b", True),
        "encoder": ("encoder", "-e", False, "encoders.txt"),
        "iterations": ("iterations", "-i", True),
        "outfile": ("outfile", "-o", True),
    }
    venom = Venom()
    for v in d.values():
        venom.set_opt(*v)
    print(venom.build_cmd())
