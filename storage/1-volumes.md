<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab: Volumes

## Step-1: Create a docker volume

```bash
$   docker volume create --name data-volume1


$   docker volume ls

$   docker volume inspect data-volume1
```

Inspect output

```console
[
    {
        "CreatedAt": "2021-09-10T13:28:13-07:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/data-volume1/_data",
        "Name": "data-volume1",
        "Options": {},
        "Scope": "local"
    }
]

```

## Step-2: Attach the volume to the container

```bash
$   docker run -it --rm -v data-volume1:/data alpine
```

## Step-3: Inspect the volume 

Inside the container, verify the volume is mounted as `/data/` directory

```bash
$   mount
```

```bash
$   mount | grep '/data'
```

```bash
$   df -kh | grep '/data'
```

## Step-4: Save some data 

```bash
$   echo "hi" > /data/a.txt
```

Exit the container by typing `exit` or `Ctrl+d`

## Step-5: Rerun the container

```bash
$   docker run -it --rm -v data-volume1:/data alpine
```

Check if the data is still there

```bash
$   ls /data
```

```bash
$   cat /data/a.txt
```

## Step-6: Start another container

In terminal-2

```bash
$   docker run -it --rm -v data-volume1:/data alpine
```

Within the container:

```bash
$   ls /data
```

you will see file a.txt

Let's create another file

```bash
$   echo 'bye' > /data/b.txt
```

In terminal-1, (container1) check the files

```bash
$   ls /data
# you should see both file a.txt and b.txt
```


So now we can share data between two containers

Exit the second container by typing `exit` or `Ctrl+d`

## Step-7: Mounting volumes as read-only

Sometimes we want the containers to only have read-only access to data (lookup data ..etc)

In terminal-2, start a new container

```bash
$   docker run -it --rm -v data-volume1:/data:ro alpine
```

Notice the `ro` flag. Inside the container, you will see the volume is mounted as read-only

```bash
$   mount | grep data
```

```console
/dev/sda2 on /data type ext4 (ro,relatime,errors=remount-ro)
```

Try to create a file

```bash
$   touch /data/c.txt
```

You will see an error message

```console
touch: /data/c.txt: Read-only file system
```
