<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab: Using Dockerhub

## Overview

Push custom images to dockerhub

## Duration 

10 mins

## Step-1: Create an account at Dockerhub

Go to [hub.docker.com](https://hub.docker.com) and create a FREE account.

Let's say your username is **`xxx`**

## Step-2: Build a custom Docker image

We will use the Dockerfile from earlier to build a custom ubuntu image

```bash
$   cd ~/docker-labs/registries

$   docker build . -t my-ubuntu
```

## Step-3: Tag the Image

Before pushing into Dockerhub we need to tag the image as follows: `username/image_name`

If your username is `xxx` the image name would be `xxx/my-ubuntu`

```bash
# replace xxx with your dockerhub username
$   docker tag my-ubuntu   xxx/my-ubuntu
```

## Step-4: Push the image to dockerhub

First you need to login to dockerhub

```bash
$   docker login
# enter your username / password
```

Now push the image

```bash
# replace xxx with your dockerhub username
$   docker push xxx/my-ubuntu
```

## Step-5: Verify the image is in using Dockerhub UI

Login to your dockerhub and verify the image is pushed in