<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab: Setting up a Local Registry

## Overview

Setup and checkin a local registry

## Duration 

10 mins

## Step-1: Registry Docker

A little fun fact, there is a actually a registry as a Docker image.

Checkout [registry](https://hub.docker.com/_/registry) on Dockerhub.

## Step-2: Run registry image

```bash
$   docker run -d -p 5000:5000 --restart always --name registry registry:2
```

Verify it is running

```bash
$   docker ps
```

You will see registry running as follows

```console
5312660fc0ae   registry:2                        "/entrypoint.sh /etc…"   5 minutes ago   Up 5 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp                                                  registry
```

## Step-3: Bulid a Custom Image

We will use the Dockerfile from earlier to build a custom ubuntu image

```bash

$   cd ~/docker-labs/registries

$   docker build . -t my-ubuntu
```

## Step-4: Tagging the Image

Before pushing an image into registry, it has to be tagged appropriately.

Here is the tagname: `localhost:5000/my-ubuntu`

- `localhost:5000` : is the registry name
- `my-ubuntu` : is the name of image

```bash
# tag syntax:
#   docker tag  src  dest
$   docker tag my-ubuntu  localhost:5000/my-ubuntu
```

## Step-5: Push the image to registry

```bash
$   docker push localhost:5000/my-ubuntu
```

Query the registry

```bash
$   curl localhost:5000/v2/_catalog
```

You should see the my-ubuntu image

```console
"repositories":["my-ubuntu"]}
```

## Step-6: Delete the local my-ubuntu image

```bash
$   docker rmi  my-ubuntu

# make sure the image is gone
$   docker images
```

## Step-7: Re-download the image from registry

```bash
$   docker pull localhost:5000/my-ubuntu

# check the image
$   docker images | grep my-ubuntu
```

```console
localhost:5000/my-ubuntu    latest               56aa3d112161   14 minutes ago   141MB
```
