# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM kalilinux/kali-linux-docker

# Install Kali dependencies
RUN apt-get update && apt-get install -y \
    metasploit-framework \ 
    python3 \
    python3-pip


LABEL Name=venominator Version=0.0.1

WORKDIR /app
ADD . /app

# Install venominator:
RUN pip3 install .
CMD ["venominator"]
