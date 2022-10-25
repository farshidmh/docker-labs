<link rel='stylesheet' href='../assets/css/main.css'/>

# Install Docker on Centos

We will install Docker on Centos

## Step 1: Install some prereqs and remove old versions

We will install a few prereqs here.  Also we will remove older versions of docker, such as "docker",
"docker-engine", and "docker.io"

```bash
sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-selinux docker-engine-selinux docker-engine

sudo yum install -y yum-utils device-mapper-persistent-data lvm
```

## Step 2: Get the GPG key and add the repository

```bash
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

Now let's do an update

```bash
sudo yum check-update
```

## Step 3: Install Docker

```bash
sudo yum install  docker-ce
```

This should install docker.  

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

## Step 5: Make a user group for Docker

We don't want to have to run docker as root every time using sudo. So let's create new group called docker,
and we will add user ec2-user to that group.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Go ahead and log out and log back in again.

## Step 5: Run Hello world container

Run the following hello world container

```bash
docker run hello-world
```

```console
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
9bb5a5d4561a: Pull complete
Digest: sha256:f5233545e43561214ca4891fd1157e1c3c563316ed8e237750d59bde73361e77
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

Seems to be going ok.  Let's see what images that got.

```bash
docker images
```

```console
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              e38bc07ac18e        5 weeks ago         1.85kB
```

Looks like things are working!
