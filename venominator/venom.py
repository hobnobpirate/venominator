#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Venom object"""

from venominator import attributes


class Venom(object):
    """Venom object stores attributes to be used in creating msfvenom payload
    
    :param arch<str>: architecture
    :param badchars<str>: list of bad characters for transform formats
    :param encoder<str>: encoder to use
    :param format<str>: output format
    :param iterations<int>: number of times to run encoder
    :param address<str>: address to call back to
    :param payload<str>: payload to build
    :param port<int>: port to listen on or call back to
    :param platform<str>: platform to build for
    :param outfile<str>: filename to output to
    :param additional<str>: additional options to add
    """

    def __init__(
        self,
        arch: str = None,
        badchars: str = None,
        encoder: str = None,
        format: str = None,
        iterations: int = None,
        address: str = None,
        payload: str = None,
        port: int = None,
        platform: str = None,
        outfile: str = None,
        additional: str = None,
    ):
        self.arch = arch
        self.badchars = badchars
        self.encoder = encoder
        self.format = format
        self.iterations = iterations
        self.address = address
        self.payload = payload
        self.port = port
        self.platform = platform
        self.outfile = outfile
        self.additional = additional

    def build_cmd(self) -> None:
        """Builds the CLI command to generate the payload"""

        cmd = "msfvenom "
        if self.arch:
            cmd += f"-a {self.arch} "
        if self.platform:
            cmd += f"--platform {self.platform} "
        if self.payload:
            cmd += f"-p {self.payload} "
        if self.address:
            cmd += f"LHOST={self.address} "
        if self.port:
            cmd += f"LPORT={self.port} "
        if self.encoder:
            cmd += f"-e {self.encoder} "
        if self.iterations:
            cmd += f"-i {self.iterations} "
        if self.format:
            cmd += f"-f {self.format} "
        if self.badchars:
            cmd += f"-b {self.badchars} "
        if self.additional:
            cmd += f"{self.additional} "
        if self.outfile:
            cmd += f"-o {self.outfile} "
        self.cmd = cmd
