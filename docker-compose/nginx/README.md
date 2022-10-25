<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab: Docker Compose 1

## Overview

Use dockercompopse

## Duration 

20 minutes

## Step-1: Install dockercompose

Follow the [install guide](https://docs.docker.com/compose/install/)

**On linux**

```bash
$   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

$   sudo chmod +x /usr/local/bin/docker-compose
```

**on mac**

Dockercompose is part of [Docker for Mac](https://docs.docker.com/desktop/mac/install/)

## Step-2: docker-compose.yaml

Let's try our nginx usecase with compose.

Inspect [docker-compose.yaml](docker-compose.yaml)

## Step-3: Bringing up nginx

**in terminal-1**

be sure to be in the right directory

```bash
$   cd ~/docker-labs/docker-compose/nginx

$   docker-compose up
```

you will see nginx starting up

```console
Starting nginx_web_1 ... done
Attaching to nginx_web_1
web_1  | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
web_1  | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
web_1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
web_1  | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
web_1  | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
web_1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
web_1  | /docker-entrypoint.sh: Configuration complete; ready for start up
```

## Step-4: Access Nginx

**in terminal-2**

```bash
$   curl localhost:8000/
```

you will get our familiar output - nginx welcome page

## Step-5: Starting in background

**on terminal-1**

Stop the docker-compose by pressing `Ctrl+c`.  It will stop the process gracefully

Let's start the process in the background.

```bash
$   cd ~/docker-labs/docker-compose/nginx

# -d to run in background
$   docker-compose up -d
```

You will notice the pricess is started in the background.

Inspect the running process

```bash
$   docker-compose ps
```

```console
$      Name                  Command               State                  Ports                
-------------------------------------------------------------------------------------------
nginx_web_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:8000->80/tcp,:::8000->80/tcp
```

You can also use `docker ps` to see running processes.

Again we can access the nginx as follows

```bash
$   curl localhost:8000/
```

## Step-6: Managing the process

We can see logs 

```bash
$   docker-compose logs

# or
$   docker-compose logs -f
```

Stop the process by

```bash
$   docker-compose down
```

```console
Stopping nginx_web_1 ... done
Removing nginx_web_1 ... done
Removing network nginx_default
```
