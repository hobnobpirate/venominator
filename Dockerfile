FROM metasploitframework/metasploit-framework

LABEL Name=venominator Version=0.0.1

ADD ./setup.py $APP_HOME
ADD venominator $APP_HOME/venominator
ENV PATH=$PATH:/usr/src/metasploit-framework/

# Install and run venominator:
RUN pip3 install .
CMD ["venominator"]