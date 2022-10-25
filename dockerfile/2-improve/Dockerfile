## TODO: fix to python 3.6
FROM python:latest

COPY README.md   README.md

# upgrade pip3
RUN  pip install --upgrade pip

RUN pip install numpy

RUN pip install pandas

# Create a user
RUN groupadd -g 1000 ubuntu && \
    useradd -rm -d /home/ubuntu -s /bin/bash -g ubuntu -u 1000 ubuntu

# set permissions for user home
RUN  mkdir -p /home/ubuntu  && \
    chown -R ubuntu:ubuntu /home/ubuntu

## TODO: login as user 'ubuntu' 
## TODO: make the working directory as '/home/ubuntu'
USER ???
WORKDIR ???

## TODO: start /bin/bash shell instead of python
