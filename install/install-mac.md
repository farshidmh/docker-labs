<link rel='stylesheet' href='../assets/css/main.css'/>

# Install Docker on Mac

There are couple of options to install Docker on Mac

1. Using Mac desktop (recommended)
2. Brew

---

## Option 1 - Mac Docker Desktop (Preferred)

Follow [instructions here](https://docs.docker.com/desktop/mac/install/)

---

## Option 2 - Using Brew

## Step 1: Install Homebrew

First test and see if you have `brew`. Open up a terminal and teyp

```bash
brew --version
```

If you don't have brew, you can then install this:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


## Step 2: Install Docker Desktop

```bash
brew tap caskroom/cask
brew cask install docker  # install Docker
open /Applications/Docker.app  # start Docker
```


## Step 3: Run Hello world container

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
