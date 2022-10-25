<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab : Imporove the Dockerfile

## Overview

Here we will improve the Dockerfile

## Duration

15 minutes

## Step-1 : Inspect the Dockerfile

```bash
# adjust your /path/to/docker-labs
$   cd ~/docker-labs/dockerfile/2-improve
```

Inspect [Dockerfile](Dockerfile)

## Step-2: Build

```bash
$   docker build .  -t my-python
```

## Step-3: Run the container

```bash
$   docker run -it my-python
```
Expect errors at this point, because of the ??? in the Dockerfile  

## Step-4: Improve the Dockerfile

Review the [Dockerfile](Dockerfile) and make improvements.

Fix TODO items and anything else you can think of.

## Step-5: Discuss your findings

Discuss with class.
