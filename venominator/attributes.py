#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Currated lists of attributes as well as helper functions

Does not currently hold all available options from msfvenom due to incomplete logic.

To get these values, run:
    msfvenom --list encoders
    msfvenom --list formats
    msfvenom --list payloads
"""

encoders = [
    "mipsbe/byte_xori",
    "mipsbe/longxor",
    "mipsle/byte_xori",
    "mipsle/longxor",
    "php/base64",
    "ppc/longxor",
    "ppc/longxor_tag",
    "ruby/base64",
    "sparc/longxor_tag",
    "x64/xor",
    "x64/xor_dynamic",
    "x64/zutto_dekiru",
    "x86/add_sub",
    "x86/alpha_mixed",
    "x86/alpha_upper",
    "x86/avoid_underscore_tolower",
    "x86/avoid_utf8_tolower",
    "x86/bloxor",
    "x86/bmp_polyglot",
    "x86/call4_dword_xor",
    "x86/context_cpuid",
    "x86/context_stat",
    "x86/context_time",
    "x86/countdown",
    "x86/fnstenv_mov",
    "x86/jmp_call_additive",
    "x86/nonalpha",
    "x86/nonupper",
    "x86/opt_sub",
    "x86/service",
    "x86/shikata_ga_nai",
    "x86/single_static_bit",
    "x86/unicode_mixed",
    "x86/unicode_upper",
    "x86/xor_dynamic",
]

# Executable formats do not take bad character arguments
ex_formats = [
    "asp",
    "aspx",
    "dll",
    "elf",
    "exe",
    "jar",
    "jsp",
    "macho",
    "osx-app",
    "war",
    "bash",
]

# Transorm formats can take bad character arguments
tr_formats = [
    "c",
    "hex",
    "java",
    "js_be",
    "js_le",
    "perl",
    "powershell",
    "python",
    "raw",
    "ruby",
    "sh",
]

formats = ex_formats + tr_formats

# Payloads list helps build out platform and arch
# platform/[arch]/...
payloads = [
    "aix/ppc/shell_bind_tcp",
    "aix/ppc/shell_reverse_tcp",
    "android/meterpreter/reverse_https",
    "android/meterpreter/reverse_tcp",
    "android/meterpreter_reverse_https",
    "android/meterpreter_reverse_tcp",
    "android/shell/reverse_https",
    "android/shell/reverse_tcp",
    "apple_ios/aarch64/meterpreter_reverse_https",
    "apple_ios/aarch64/meterpreter_reverse_tcp",
    "apple_ios/aarch64/shell_reverse_tcp",
    "apple_ios/armle/meterpreter_reverse_https",
    "apple_ios/armle/meterpreter_reverse_tcp",
    "bsd/sparc/shell_bind_tcp",
    "bsd/sparc/shell_reverse_tcp",
    "bsd/vax/shell_reverse_tcp",
    "bsd/x64/shell_bind_tcp",
    "bsd/x64/shell_reverse_tcp",
    "bsd/x86/shell/bind_tcp",
    "bsd/x86/shell/reverse_tcp",
    "bsd/x86/shell_bind_tcp",
    "bsd/x86/shell_reverse_tcp",
    "bsdi/x86/shell/bind_tcp",
    "bsdi/x86/shell/reverse_tcp",
    "bsdi/x86/shell_bind_tcp",
    "bsdi/x86/shell_find_port",
    "bsdi/x86/shell_reverse_tcp",
    "java/jsp_shell_bind_tcp",
    "java/jsp_shell_reverse_tcp",
    "java/meterpreter/bind_tcp",
    "java/meterpreter/reverse_https",
    "java/meterpreter/reverse_tcp",
    "java/shell/bind_tcp",
    "java/shell/reverse_tcp",
    "java/shell_reverse_tcp",
    "linux/aarch64/meterpreter/reverse_tcp",
    "linux/aarch64/meterpreter_reverse_https",
    "linux/aarch64/meterpreter_reverse_tcp",
    "linux/aarch64/shell/reverse_tcp",
    "linux/aarch64/shell_reverse_tcp",
    "linux/armbe/meterpreter_reverse_https",
    "linux/armbe/meterpreter_reverse_tcp",
    "linux/armbe/shell_bind_tcp",
    "linux/armle/meterpreter/bind_tcp",
    "linux/armle/meterpreter/reverse_tcp",
    "linux/armle/meterpreter_reverse_https",
    "linux/armle/meterpreter_reverse_tcp",
    "linux/armle/shell/bind_tcp",
    "linux/armle/shell/reverse_tcp",
    "linux/armle/shell_bind_tcp",
    "linux/armle/shell_reverse_tcp",
    "linux/mips64/meterpreter_reverse_https",
    "linux/mips64/meterpreter_reverse_tcp",
    "linux/mipsbe/meterpreter/reverse_tcp",
    "linux/mipsbe/meterpreter_reverse_https",
    "linux/mipsbe/meterpreter_reverse_tcp",
    "linux/mipsbe/shell/reverse_tcp",
    "linux/mipsbe/shell_bind_tcp",
    "linux/mipsbe/shell_reverse_tcp",
    "linux/mipsle/meterpreter/reverse_tcp",
    "linux/mipsle/meterpreter_reverse_https",
    "linux/mipsle/meterpreter_reverse_tcp",
    "linux/mipsle/shell/reverse_tcp",
    "linux/mipsle/shell_bind_tcp",
    "linux/mipsle/shell_reverse_tcp",
    "linux/ppc/meterpreter_reverse_https",
    "linux/ppc/meterpreter_reverse_tcp",
    "linux/ppc/shell_bind_tcp",
    "linux/ppc/shell_reverse_tcp",
    "linux/ppc64/shell_bind_tcp",
    "linux/ppc64/shell_reverse_tcp",
    "linux/ppc64le/meterpreter_reverse_https",
    "linux/ppc64le/meterpreter_reverse_tcp",
    "linux/ppce500v2/meterpreter_reverse_https",
    "linux/ppce500v2/meterpreter_reverse_tcp",
    "linux/x64/meterpreter/bind_tcp",
    "linux/x64/meterpreter/reverse_tcp",
    "linux/x64/meterpreter_reverse_https",
    "linux/x64/meterpreter_reverse_tcp",
    "linux/x64/shell/bind_tcp",
    "linux/x64/shell/reverse_tcp",
    "linux/x64/shell_bind_tcp",
    "linux/x64/shell_reverse_tcp",
    "linux/x86/meterpreter/bind_tcp",
    "linux/x86/meterpreter/reverse_tcp",
    "linux/x86/meterpreter_reverse_https",
    "linux/x86/meterpreter_reverse_tcp",
    "linux/x86/shell/bind_tcp",
    "linux/x86/shell/reverse_tcp",
    "linux/x86/shell_bind_tcp",
    "linux/x86/shell_reverse_tcp",
    "linux/zarch/meterpreter_reverse_https",
    "linux/zarch/meterpreter_reverse_tcp",
    "nodejs/shell_bind_tcp",
    "nodejs/shell_reverse_tcp",
    "nodejs/shell_reverse_tcp_ssl",
    "osx/armle/shell/bind_tcp",
    "osx/armle/shell/reverse_tcp",
    "osx/armle/shell_bind_tcp",
    "osx/armle/shell_reverse_tcp",
    "osx/ppc/shell/bind_tcp",
    "osx/ppc/shell/reverse_tcp",
    "osx/ppc/shell_bind_tcp",
    "osx/ppc/shell_reverse_tcp",
    "osx/x64/meterpreter/bind_tcp",
    "osx/x64/meterpreter/reverse_tcp",
    "osx/x64/meterpreter_reverse_https",
    "osx/x64/meterpreter_reverse_tcp",
    "osx/x64/shell_bind_tcp",
    "osx/x64/shell_reverse_tcp",
    "osx/x86/shell_bind_tcp",
    "osx/x86/shell_find_port",
    "osx/x86/shell_reverse_tcp",
    "php/meterpreter/bind_tcp",
    "php/meterpreter/reverse_tcp",
    "php/meterpreter_reverse_tcp",
    "python/meterpreter/bind_tcp",
    "python/meterpreter/reverse_https",
    "python/meterpreter/reverse_tcp",
    "python/meterpreter_bind_tcp",
    "python/meterpreter_reverse_https",
    "python/meterpreter_reverse_tcp",
    "python/shell_bind_tcp",
    "python/shell_reverse_tcp",
    "python/shell_reverse_udp",
    "r/shell_bind_tcp",
    "r/shell_reverse_tcp",
    "ruby/shell_bind_tcp",
    "ruby/shell_reverse_tcp",
    "solaris/sparc/shell_bind_tcp",
    "solaris/sparc/shell_reverse_tcp",
    "solaris/x86/shell_bind_tcp",
    "solaris/x86/shell_reverse_tcp",
    "windows/meterpreter/reverse_https",
    "windows/meterpreter/reverse_tcp",
    "windows/meterpreter_bind_tcp",
    "windows/meterpreter_reverse_https",
    "windows/meterpreter_reverse_tcp",
    "windows/powershell_bind_tcp",
    "windows/powershell_reverse_tcp",
    "windows/shell/bind_tcp",
    "windows/shell/reverse_tcp",
    "windows/shell/reverse_udp",
    "windows/shell_bind_tcp",
    "windows/shell_reverse_tcp",
    "windows/x64/meterpreter/bind_tcp",
    "windows/x64/meterpreter/reverse_https",
    "windows/x64/meterpreter/reverse_tcp",
    "windows/x64/meterpreter_bind_tcp",
    "windows/x64/meterpreter_reverse_https",
    "windows/x64/meterpreter_reverse_tcp",
    "windows/x64/powershell_bind_tcp",
    "windows/x64/powershell_reverse_tcp",
    "windows/x64/shell/bind_tcp",
    "windows/x64/shell/reverse_tcp",
    "windows/x64/shell_bind_tcp",
    "windows/x64/shell_reverse_tcp",
]

# These platforms do not specify an architecture
no_arch = ["android", "java", "nodejs", "python", "r", "ruby"]


def make_dict(v: list) -> dict:
    """Make an alphabetically sorted dictionary from a list

    :param v<list>: list of an attribute type
    :return <dict>: in format {1: v[0], 2: v[1], ...}
    """
    k = list(range(1, len(v) + 1))
    return dict(zip(k, sorted(v)))


def list_platforms() -> dict:
    """Provides a dictionary of available platforms

    From payloads list, extracts the first element as split by `/` as the platform.
    Creates a unique set of platforms and returns a dictionary of them.

    :return <dict>: Alphabetically sorted dict of platforms supported
    """
    v = set()
    for payload in payloads:
        v.add(payload.split("/")[0])
    return make_dict(list(v))


def list_encoders(arch: str) -> dict:
    """Provides a dictionary of available encoders

    From encoders list, creates a unique set of encoders and returns a dictionary of them.
    Only encoders with the selected architecture are returned.

    :param arch<sr>: architecture selected, filters the encoders
    :return <dict>: Alphabetically sorted dict of encoders supported
    """
    v = []
    for encoder in encoders:
        if arch in encoder:
            v.append(encoder)
    if v:
        return make_dict(v)
    else:
        return None


def list_formats() -> dict:
    """Provides a dictionary of available formats

    From formats list, creates a dict of platforms.

    :return <dict>: Alphabetically sorted dict of formats supported
    """
    return make_dict(formats)


def list_arches(platform: str) -> dict:
    """Provides a dictionary of available architectures

    From payloads list, extracts the second element as split by `/`.
    Creates a dict of architectures which match the platform.
    
    Windows x86 does not list the architecture in the payload list, so it is assumed
    that if it is Windows and not x64, then x86 should be the arch.

    Some platforms (listed in no_arch) do not contain architectures. In this case, NoneType is returned.


    :return <dict>: Alphabetically sorted dict of architectures supported
    """
    if platform in no_arch:
        return None
    elif platform == "windows":
        return make_dict(["x86", "x64"])
    
    v = set()
    
    for payload in payloads:
        if platform in payload:
            v.add(payload.split("/")[1])
    
    return make_dict(list(v))


def filter_payloads(platform: str, arch: str = None) -> dict:
    """Filters payloads available based on platform and architecture.

    Windows x86 does not list the architecture in the payload list, so it is assumed
    that if it is Windows and not x64, then x86 should be the arch.

    Some platforms (listed in no_arch) do not contain architectures. In this case, arch is ignored.

    :param platform<str>: Selected platform to filter on
    :param arch<str>: Selected architecture to filter on
    :return <dict>: Dictionary of filtered payloads
    """
    v = []
    
    if platform == "windows" and arch == "x86":
        for payload in payloads:
            if platform in payload:
                if payload.split("/")[0] == platform and not "x64" in payload:
                    v.append(payload)
    
    elif platform in no_arch:
        for payload in payloads:
            if payload.split("/")[0] == platform:
                v.append(payload)
    
    else:
        for payload in payloads:
            if payload.split("/")[0] == platform and arch in payload:
                v.append(payload)
    
    return make_dict(v)
