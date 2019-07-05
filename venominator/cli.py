#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

from venominator.venom import Venom

@click.command()
def cli():
    """Command line interface for Mach O Peek"""
    venom = Venom()
    venom.set_arch()
    venom.set_platform()
    venom.set_payload()
    venom.set_encoder()
    venom.set_format()
    venom.set_bad_chars()
    venom.set_outfile()
    venom.build_payload()

if __name__ == "__main__":
    cli()