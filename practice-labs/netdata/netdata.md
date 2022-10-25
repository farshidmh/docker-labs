<link rel='stylesheet' href='../../assets/css/main.css'/>

# Netdata

[Netdata home](https://github.com/netdata/netdata)

[Netdata docker guide](https://learn.netdata.cloud/docs/agent/packaging/docker/)

docker-compose is the easiest way to run it.

```bash

# start
$   docker-compose up -d

# go to http://localhost:19999

# stop
$  docker-compose down
```

## Monitoring A Process

Go to `Applications --> Processes` and find the process