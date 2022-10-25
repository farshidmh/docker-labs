<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab: User Defined Networking

## Overview

In this lab, we are going to create and use a 'user-defined network'

## Duration 

15 minutes

## Step-1: See Docker Networks

```bash
$   docker network ls
```

You should see 3 default networks created by Docker

```console
NETWORK ID     NAME                DRIVER    SCOPE
dc09a3699c8f   bridge              bridge    local
71347a332fe7   host                host      local
d28a41f8631c   none                null      local
```

## Step-2: Create a new Network

```docker
$   docker network create --driver bridge my-network
$   docker network ls

# get more details
$   docker network inspect my-network
```

You should see our network listed


```console
NETWORK ID     NAME                DRIVER    SCOPE
dc09a3699c8f   bridge              bridge    local
71347a332fe7   host                host      local
d28a41f8631c   none                null      local
cb70ddcf0587   my-network          bridge    local
```

## Step-3: Start a couple of containers on our network

Start nginx, but no port mapping!

```bash
# nginx
$   docker run --rm -d --network my-network  --name nginx1  nginx

# busybox
$   docker run -it --rm   --network my-network   busybox
```

## Step-4: Access nginx from busybox

Access nginx from busybox

```bash
# from within busybox container

$  ping nginx1

$   wget -O -   nginx1:80/
```

You should see both ping and wget are able to access `nginx`. 

This is possible because docker is running a DNS server, resolving container names to IPs
