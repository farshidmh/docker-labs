<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab: Container 2

We are going to see how we can manipulate our containers.

## Step 1: Start up a new alpine container

```bash
$   docker container run -it alpine
```

You will find yourself a root prompt in the new container. Try executing the command "ls /"

```bash
$ ls /
```

```console
bin  dev  etc  home lib  media  mnt  proc 
root run  sbin srv  sys  tmp  usr  var
```

## Step 2: Create a new file

```bash
$   echo  "hi" > a.txt
$   ls 
# you should see 'a.txt'
```

**=> Exit out of your container by hitting control-D**

Now, let's see what happens if we run our container again.

```bash
$   docker container run -it alpine
```

Ok, let's see if our files are there

```bash
$   ls 
```

```console
bin  dev  etc  home lib  media  mnt  proc 
root run  sbin srv  sys  tmp  usr  var
```

**=> We don't see the file 'a.txt' we just created**

Because the containers are isolated and the changes we make within containers are **not** persisted.

Go ahead and exit by hitting CNTRL-D or typing exit.

## Step-3: Exec

Start a container

```bash
$    docker container run -it alpine

## now you will be in the continer:
## crate a file
    >  touch a.txt
```

**Keep this continer running, do not exit!**

**ACTION: Open another terminal, and execute this command**

```bash
$   docker ps
# note the container id of you the running alpine container
# say 'aaabbbccc'

## Execute a command in that container
## Substitute CONTAINER_ID with the actual container id
$   docker exec CONTAINER_ID   ls
```

You should see the file `a.txt`

## Step 4: Deleting Containers

Now, see if you can see your command:

```bash
$ docker ps -a
```

```console
CONTAINER ID   IMAGE     COMMAND        CREATED             STATUS                     PORTS     NAMES               SIZE
c183852a7215   alpine    "/bin/sh"      6 minutes ago       Exited (0) 2 minutes ago             adoring_joliot      5B (virtual 4.15MB)
```

Notice the size. 5 bytes. Not exactly taking up a lot of space.  The container IMAGE takes up 4.15MB.

But, we may want to clean up our images anyway. We can use docker container rm for that.

```bash
$   docker container rm <container-id>
```

And you can now run docker container ls -as

```console
CONTAINER ID   IMAGE     COMMAND        CREATED             STATUS                     PORTS     NAMES               SIZE
```

It shouldn't be there anymore.

What if you want to run the docker container and just have it auto-delete after you are done.

## Step-5: Deleting all stopped containers

```bash
# get all container ids
$   docker ps -aq

$   docker rm $(docker ps -aq)

## force
$   docker rm -f $(docker ps -aq)
```

## Step-6: Deleting Images

Let's delete the alpine image locally.  We can always pull it from DockerHub.

```bash
$   docker images

$   docker image rm alpine
# or
$   docker rmi alpine

# list images again
$   docker images
#  alpine should be gone
```
