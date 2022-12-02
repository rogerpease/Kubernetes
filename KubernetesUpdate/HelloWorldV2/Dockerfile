FROM ubuntu:20.04

RUN apt-get update 
RUN apt-get -y install python3-pip python3-flask bash net-tools
RUN pip3 install flask  
COPY HelloWorldApp.py .
CMD ["./HelloWorldApp.py"]
