<link rel='stylesheet' href='../assets/css/main.css'/>

# Creating a Custom Image

## Overview

We will create a custom image manually

## Duration

10 mins

## Step-1: Run a basic ubuntu image

```bash
$   docker run -it  --name ubuntu-c1 ubuntu
```

Inside the container:

```bash
# try the tree command
$   tree
# it is not there

# install tree
$   apt update
$   apt install tree
$   exit
```

Now `ubuntu-c1`  container is stopped

## Step-2: See What Changed

```bash
$   docker diff ubuntu-c1
```

You should see a bunch of files that are changed.  You will see bunch of apt files changed.  And also `/usr/bin/tree` binary

## Step-3: Save the Container

Save the container as a new image `ubuntu1`

```bash
$   docker commit -m "added tree" ubuntu-c1  ubuntu1
```

See the custom image

```bash
$   docker images | grep ubuntu
```

You may see an output like:

```console
ubuntu1                                         latest              65c5bf73dd89   6 minutes ago   104MB
ubuntu                                          latest              f63181f19b2f   7 months ago    72.9MB
```

You can see that

- our image `ubuntu1` is newer
- and image size is larger (due to added files)

## Step-4 : Run our new Image

```bash
$   docker run -it ubuntu1

# run tree command
$   tree
# you will see the output
```