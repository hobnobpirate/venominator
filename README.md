# Venominator

This script provides a CLI driven menu for msfvenom in order to assist with the creation of shellcode or other msfvenom payloads.

## Requirements

- Python3
- While `msfvenom` is not required to run the script, it will be required in order to run the output. Get it by installing the [Metasploit Framework](https://www.metasploit.com).

## Installation

First, clone the repo:

```bash
git clone git@github.com:hobnobpirate/venominator.git
cd venominator
```

### Docker

There is a Kali Docker image that can be setup to run this script if you want to test the output function.
If you cloned the repo, the Dockerfile is included.
To build the Docker container, run:

```bash
docker build --rm -f "Dockerfile" -t venominator:latest .
```

This will download the Kali docker image and install all necessary requirements (metasploit and Python3).
Once you've built the container, you can run *venominator* by running the container with:

```bash
docker run --rm -it -v "$(pwd)"/Payloads:/app/ venominator
```

While the bind mount is not strictly necessary, it will allow you to have access to the generated payload on your host machine.
It should be saved in the *./Payloads* directory on your host.

### Without Docker

If you are running this program on a host that either has Metasploit installed or you do not want to generate a payload the script will still run in standalone mode.
You can either install it into your own (virtual) environment:

```bash
pip install -e .
```

or run it without installing:

```bash
pip install -r requirements.txt
python venominator/cli.py
```

## Usage

Once you have launched the program via the Docker container or command line, the whole program is menu driven.
Use the menu to select the options you'd like to use.
If you have *msfvenom* installed on your host or are using the provided Docker container, you will have the option to create the payload.
If you select **yes** on that step the payload will be generated.
A log file is also created to document the command you ran to create the payload.
