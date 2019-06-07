# Module 1 - Venominator

[Repo](https://github.com/hobnobpirate/CSC842/tree/master/Module1)

This script provides a CLI driven menu for msfvenom in order to assist with the creation of shellcode or other msfvenom payloads.

## Requirements:

- Python3
- While `msfvenom` is not required to run the script, it will be required in order to run the output. Get it by installing the [Metasploit Framework](https://www.metasploit.com).

## Usage:

```bash
python3 venominator.py
```

Menu items can be skipped by simply pressing *Enter/Return*.

## Future Work:

- Filtering subsequent menus based on previous input (i.e. only display Windows 64-bit payloads if those options were selected).

- Add option to create the payload at the end of the script (trivial).

- Allow script to accept json configuration file (trivial).

## Video Demo:

[Demo](https://youtu.be/OoQAJIFVk3E)
