<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab : Container 3

## Overview

Attach to running containers

## Runtime

10 mins

## Step-1: Start a long running container

In previous examples, our containers exited as soon as the task is done.  In this lab, let's run a container that will keep running

Run a container in background

```bash
$    docker run -d alpine /bin/sh -c "while true; do sleep 3; date; done"
```

Here `-d` flag puts the container in the background

## Step-2: Inspect the Running Containers

```bash
$   docker ps
```

## Step-3: See the output of background container

```bash
# replace container_id with the actual id
$   docker logs   CONTAINER_ID
```

To follow the logs

```bash
$   docker  logs  -f   CONTAINER_ID
```

## Step-4: Attach to a background container

```bash
$   docker container attach CONTAINER_ID
```

## Step-5: Pausing and Resuming

On terminal 1:

```bash
$  docker run  alpine /bin/sh -c "while true; do sleep 1; date; done"
# leave it running
```

On terminal 2:

```bash
$   docker ps
# note the container id of running container

$   docker pause CONTAINER_ID
```

Observe how the output from terminal-1 is now paused.

Unpause the container

```bash
$   docker   unpause CONTAINER_ID
```

Now observe how the output from terminal-1 is resumed.

Let's stop the container.

ON terminal-2

```bash
$   docker stop CONTAINER_ID
```