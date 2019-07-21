# Venominator

This script provides a CLI driven menu for msfvenom in order to assist with the creation of shellcode or other msfvenom payloads.

## Requirements

- Python3
- While `msfvenom` is not required to run the script, it will be required in order to run the output. Get it by installing the [Metasploit Framework](https://www.metasploit.com).

## Installation

First, clone the repo:

```bash
git clone https://github.com/hobnobpirate/venominator.git
cd venominator
```

Next, either use Docker (recommended method) or a virtual environment to install and run venominator.

### Docker

There is a Metasploit Framework Docker image that can be setup to run this script if you want to test the output function.
If you cloned the repo, the Dockerfile is included.
To build the Docker container, run:

```bash
docker build --rm -f "Dockerfile" -t venominator:latest .
```

This will download the Metasploit Framework Docker image and install venominator in it.
Once you've built the container, you can run *venominator* by running the container with:

```bash
docker run --rm -it -v "$(pwd)"/payloads:/payloads venominator
```

While the bind mount is not strictly necessary, it will allow you to have access to the generated payload on your host machine.
It should be saved in the *./payloads* directory on your host.

### Without Docker

If you are running this program on a host that either has Metasploit installed or you do not want to generate a payload the script will still run in standalone mode.
You can install it into your own virtual environment (Debian/Ubuntu steps shown):

```bash
sudo apt install python3-venv -y
python3 -m venv test
source test/bin/activate
pip install -e .
venominator
```

## Usage

Once you have launched the program via the Docker container or command line, the whole program is menu driven.
Use the menu to select the options you'd like to use.
If you have *msfvenom* installed on your host or are using the provided Docker container, you will have the option to create the payload.
If you select **yes** on that step the payload will be generated.
A log file is also created to document the command you ran to create the payload.
