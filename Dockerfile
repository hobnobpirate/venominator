FROM kalilinux/kali-linux-docker

# Install Kali dependencies
RUN apt-get update && apt-get install -y \
    metasploit-framework \ 
    python3 \
    python3-pip


LABEL Name=venominator Version=0.0.1

WORKDIR /app
ADD . /app

# Install and run venominator:
RUN pip3 install .
CMD ["venominator"]
