<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab: Container 1

## Overview

When we run a docker container, we rarely ever start from scratch. Docker provides us an OS kernel
(such as Linux), but generally does **not** provide us with any of the other aspects of the OS we
think of.  

## Step 1: Do a Docker Pull

`Docker pull` will pull down a public repo from dockerhub. Think of it like a git pull.

We are going to use a lightweight Linux container called [alpine](https://hub.docker.com/r/_/alpine/).

It is only 5 MB in size, making it perfect for a containers.

```bash
docker pull alpine
```

You should get the results: 

```console
Using default tag: latest
latest: Pulling from library/alpine
213ec9aee27d: Pull complete
Digest: sha256:bc41182d7ef5ffc53a40b044e725193bc10142a1243f395ee852a8d9730fc2ad
Status: Downloaded newer image for alpine:latest
docker.io/library/alpine:latest
```

## Step 2: See the docker image we downloaded

```bash
docker images
```

Output will look like

```console
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
alpine        latest    9c6f07244728   3 weeks ago     5.54MB
hello-world   latest    feb5d9fea6a5   11 months ago   13.3kB
```

There you see it. Alpine, But what do we do with it?

## Step 3: Run the Container

How do we run the container?

```bash
docker run alpine ls
```

As we are in the root `/` directory, we see the directories there.

```console
bin
dev
etc
home
lib
media
mnt
proc
root
run
sbin
srv
sys
tmp
usr
var
```

## Step 4: Listing Containers

Let us try to list our container.  

```bash
docker container ls
```
or 

```bash
docker ps
```
response:

```console
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

**Wait??** Where's our container? Well, our container isn't running now. The command we gave it (ls) ended already. We can see the stopped container if we want like this.

```bash
docker container ls -a
```
or
```bash
docker ps -a
```

Output:
```console
CONTAINER ID   IMAGE         COMMAND    CREATED              STATUS                          PORTS     NAMES
c37a45ce6270   alpine        "ls"       About a minute ago   Exited (0) About a minute ago             brave_galois
bff3d8a7c2c6   hello-world   "/hello"   54 minutes ago       Exited (0) 54 minutes ago                 friendly_ride
```

There we go. We have two containers, both stopped. Remember hello world? That's there. Just stopped. 

Wait, should we keep creating all these containers? You can stop it from being created if you just want to
one-and-done a command.

```bash
docker container run --rm alpine  ls -l
```

**=> TODO: See if what containers we have. Does the new one show up?**

## Step 5: Interactive shells

Wait, how do I ssh to my container? Well, you don't usually do it that way. For one thing, your container
isn't actually running right now, so if you try to ssh it won't respond. What you probably want is an
interactive shell.

How do I do that?

```bash
docker run -it --rm alpine /bin/ash
```
or
```bash
docker container run -it --rm alpine /bin/ash
```

What does this mean?
 * `-i`: interactive mode
 * `-t`: terminal mode
 * `--rm`: remove container after we are done
 * `/bin/ash`: bash is big and needs to be installed.  ash (almquist shell) is small. We also have old-school sh.

Here is the results with a few commands:

```console
/ # echo hello
hello
/ # cd
~ # pwd
/root
~ # echo bye!
bye!
~ # exit
```

**=> TODO: You try some of your own commands.**

## Summary

So what's the point? That we can run a mini size linux? Well, we are about to see how we can build
on top of this. But usually we need to start somewhere, and we created some basic place to start. 

---
Verified by Farshid on 2022-08-31 16:05:00 UTC
