Architectures = {
    1: "x64",
    2: "x86",
}

Encoders_x64 = {
    1: "x64/xor",
    2: "x64/xor_dynamic",
    3: "x64/zutto_dekiru",
}

Encoders_x86 = {
    1: "x86/add_sub",
    2: "x86/alpha_mixed",
    3: "x86/alpha_upper",
    4: "x86/avoid_underscore_tolower",
    5: "x86/avoid_utf8_tolower",
    6: "x86/bloxor",
    7: "x86/bmp_polyglot",
    8: "x86/call4_dword_xor",
    9: "x86/context_cpuid",
    10: "x86/context_stat",
    11: "x86/context_time",
    12: "x86/countdown",
    13: "x86/fnstenv_mov",
    14: "x86/jmp_call_additive",
    15: "x86/nonalpha",
    16: "x86/nonupper",
    17: "x86/opt_sub",
    18: "x86/service",
    19: "x86/shikata_ga_nai",
    20: "x86/single_static_bit",
    21: "x86/unicode_mixed",
    22: "x86/unicode_upper",
    23: "x86/xor_dynamic",
}

Formats_Win = {
    1: "asp",
    2: "aspx",
    3: "dll",
    4: "exe",
    5: "c",
    6: "hex",
    7: "python",
    8: "raw",
}

Formats_Nix = {
    1: "elf",
    2: "c",
    3: "hex",
    4: "python",
    5: "raw",
    6: "sh",
}

Payloads_Win_x86 = {
    1: "windows/meterpreter/bind_tcp",
    2: "windows/meterpreter/reverse_http",
    3: "windows/meterpreter/reverse_https",
    4: "windows/meterpreter/reverse_tcp",
    5: "windows/meterpreter_bind_tcp",
    6: "windows/meterpreter_reverse_http",
    7: "windows/meterpreter_reverse_https",
    8: "windows/meterpreter_reverse_tcp",
    9: "windows/shell/bind_tcp",
    10: "windows/shell/reverse_tcp",
    11: "windows/shell_bind_tcp",
    12: "windows/shell_reverse_tcp",
}

Payloads_Win_x64 = {
    1: "windows/x64/meterpreter/bind_tcp",
    2: "windows/x64/meterpreter/reverse_http",
    3: "windows/x64/meterpreter/reverse_https",
    4: "windows/x64/meterpreter/reverse_tcp",
    5: "windows/x64/meterpreter_bind_tcp",
    6: "windows/x64/meterpreter_reverse_http",
    7: "windows/x64/meterpreter_reverse_https",
    8: "windows/x64/meterpreter_reverse_tcp",
    9: "windows/x64/shell/bind_tcp",
    10: "windows/x64/shell/reverse_tcp",
    11: "windows/x64/shell_bind_tcp",
    12: "windows/x64/shell_reverse_tcp",
}

Payloads_Nix_x64 = {
    1: "linux/x64/meterpreter/bind_tcp",
    2: "linux/x64/meterpreter/reverse_tcp",
    3: "linux/x64/meterpreter_reverse_http",
    4: "linux/x64/meterpreter_reverse_https",
    5: "linux/x64/meterpreter_reverse_tcp",
    6: "linux/x64/shell/bind_tcp",
    7: "linux/x64/shell/reverse_tcp",
    8: "linux/x64/shell_bind_tcp",
    9: "linux/x64/shell_reverse_tcp",
}

Payloads_Nix_x86 = {
    1: "linux/x86/meterpreter/bind_tcp",
    2: "linux/x86/meterpreter/reverse_tcp",
    3: "linux/x86/meterpreter_reverse_http",
    4: "linux/x86/meterpreter_reverse_https",
    5: "linux/x86/meterpreter_reverse_tcp",
    6: "linux/x86/shell/bind_tcp",
    7: "linux/x86/shell/reverse_tcp",
    8: "linux/x86/shell_bind_tcp",
    9: "linux/x86/shell_reverse_tcp",
}

Platforms = {
    1: "Linux",
    2: "Windows",
}