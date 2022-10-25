## Ubuntu 20.04
FROM ubuntu:focal

ENV SHELL           /bin/bash

## for apt-get to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

## update apt system
RUN apt-get update --fix-missing -yq && \
        apt-get -yq upgrade

# install a bunch of packages
RUN apt install -y \
        iputils-ping \
        tree

## --- cleanup apt
RUN rm -f /etc/apt/apt.conf.d/01proxy  && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# copy some files
COPY README.md   /
