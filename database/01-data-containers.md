# Data Containers


## Overview

There are two ways of approaching stateful Containers, that is containers are store and persistent data for future use. This could be the container creating and storing data, for example, a database. Alternatively, it could be data requiring additional for instance the configuration or SSL certifications. This approach can also be used to backup data or debug containers.

One approach we've discussed is using the `-v <host-dir>:<container-dir>` option to map directories. The other approach is to use Data Containers. This scenario will introduce the advantages of using Data Containers.



## Step 1 - Create Container

Data Containers are containers whose sole responsibility is to be a place to store/manage data.

Like other containers they are managed by the host system. However, they don't run when you perform a docker ps command.

To create a Data Container we first create a container with a well-known name for future reference. We use busybox as the base as it's small and lightweight in case we want to explore and move the container to another host.

When creating the container, we also provide a -v option to define where other containers will be reading/saving data.

Create a Data Container for storing configuration files using:

```bash
docker create -v /config --name dataContainer busybox
```

## Step 2 -- Copy Files

With the container in place, we can now copy files from our local client directory into the container.

To copy files into a container you use the command `docker cp`. The following command will copy the `config.conf` file into our dataContainer and the directory config.

```bash
docker cp config.conf dataContainer:/config/
```

## Step 3 -- Mount Volumes

Now our Data Container has our config, we can reference the container when we launch dependent containers requiring the configuration file.

Using the `--volumes-from <container>` option we can use the mount volumes from other containers inside the container being launched. In this case, we'll launch an Ubuntu container which has reference to our Data Container. When we list the config directory, it will show the files from the attached container.

```bash
docker run --volumes-from dataContainer ubuntu ls /config
```

If a `/config` directory already existed then, the volumes-from would override and be the directory used. You can map multiple volumes to a container.


## Step 4 -- Export / Import Containers

If we wanted to move the Data Container to another machine then we can export it to a `.tar` file.

```bash
docker export dataContainer > dataContainer.tar
```

The following command will import that back into the container

```bash
docker import dataContainer.tar
```









