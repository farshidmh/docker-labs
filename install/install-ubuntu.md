<link rel='stylesheet' href='../assets/css/main.css'/>

# Install Docker on Ubuntu

We will install Docker on Ubuntu 18.04 +

## Step 1: Install some pre-requirements and remove old versions

We will install a few pre-requirements here. Also, we will remove older versions of docker, such as `docker`,
`docker-engine`, and `docker.io`

```bash
sudo apt-get install curl
```

```bash
sudo apt-get remove docker docker-engine docker.io
```

## Step 2: Get the GPG key and add the repository

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

Now let's do an update

```bash
sudo apt-get update
```

## Step 3: Install Docker

```bash
sudo apt-get install -y docker-ce
```

This should install “docker”.

## Step 4: Verify Docker is running

```bash
sudo systemctl status docker
```

The output should be as follows:

```console
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2018-05-18 00:45:54 UTC; 10s ago
     Docs: https://docs.docker.com
 Main PID: 31400 (dockerd)
   CGroup: /system.slice/docker.service
           ├─31400 /usr/bin/dockerd -H fd://
           └─31408 docker-containerd --config /var/run/docker/containerd/containerd.toml
```

*** `active (running)` would be a good indicator that Docker is running, and it should be in green. ***

## Step 5: Make a user group for Docker

We don't want to have to run docker as root every time using sudo. So let's create a new group called docker,
and we will add user ubuntu to that group.

```bash
sudo groupadd docker
```

```bash
sudo usermod -aG docker $USER
```

## Step 6: Log out and log back in again

This is necessary for group changes to take effect

## Step 7: Run Hello world container

Run the following hello world container

```bash
docker run hello-world
```

Result:

```console
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:7d246653d0511db2a6b2e0436cfd0e52ac8c066000264b3ce63331ac66dca625
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

Seems to be going ok. Let's see what images that got.

```bash
docker images
```

```console
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    feb5d9fea6a5   11 months ago   13.3kB
```

Looks like things are working!

---
Verified by Farshid on 2022-08-31 13:12:00 UTC