#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Venom object"""

from venominator import attributes


class Venom(object):
    """Venom object stores attributes to be used in creating msfvenom payload"""

    def __init__(self):
        self.arch = None
        self.badchars = None
        self.encoder = None
        self.format = None
        self.iterations = None
        self.address = None
        self.payload = None
        self.port = None
        self.platform = None
        self.outfile = None
        self.additional = None

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
