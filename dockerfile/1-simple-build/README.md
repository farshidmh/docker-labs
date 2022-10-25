<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab: Build a Simple Docker Image

## Step-1: Inspect the Dockerfile

Be sure to be in `docker-labs/dockerfile/1-simple-build` directory

```bash
# adjust to /path/to/docker-labs
cd  ~/docker-labs/dockerfile/1-simple-build
```

[Dockerfile is here](Dockerfile)

## Step-2: Build

```bash
$   time docker build . -t my-ubuntu
```

## Step-3: Run the newly created image

```bash
$   docker run -it --rm my-ubuntu
```

This will drop you into / directory

Examine file `README.md`

```bash
# inside the container
$   less  README.md
```

## Step-4: Install more packages

We are going to install `atop` package

- Edit the [Dockerfile](Dockerfile) (use `vi` or `nano`)


- Around line number 15, add another packge `atop`, so the final line looks like this

```text
RUN apt install -y \
        atop \
        iputils-ping \
        tree
```

- Build again

```bash
$   time docker build . -t my-ubuntu
```

**ACTION: Note which steps are cached and which steps are executed**

## Step-5: Run the newly built container

```bash
$   docker run -it  --rm my-ubuntu

# run atop
$   atop
```

Exit by typing `exit` or `Ctrl+d`

## Step-6: Install another package

- Edit [Dockerfile](Dockerfile)

- In the last step, we modified an existing RUN command

- Here we will try to add a new RUN command, like this

```text
RUN apt install -y less
```

- Save the file and build again

- Observe the behaviour

## Discussion

As we note, each `RUN` commnad will create a separate layer.

We don't want to create too many layers with just one change!

Also we may not want to create an 'uber layer' with tons of changes.

Look at [Nginx Dockerfile](https://github.com/nginxinc/docker-nginx/blob/master/stable/debian/Dockerfile)  and see how they are doing it.

**Discuss with class.**

