FROM metasploitframework/metasploit-framework

LABEL Name=venominator Version=0.0.1

WORKDIR /app
ADD . /app
ENV PATH=$PATH:/usr/src/metasploit-framework/

# Install and run venominator:
RUN pip3 install .
ENTRYPOINT [ "" ]
CMD ["venominator"]