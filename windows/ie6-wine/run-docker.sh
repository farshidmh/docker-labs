#!/bin/bash


#DOCKER_IMAGE="elephantscale/ie6:latest"


if ! docker volume ls -qf "name=winehome" | grep -q "winehome"; then
    echo "INFO: Creating Docker volume container 'winehome'..."
    docker volume create winehome
else
    echo "INFO: Using existing Docker volume container 'winehome'..."
fi

docker run -it \
--rm \
--env="DISPLAY" \
--volume="${XAUTHORITY}:/root/.Xauthority:ro" \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:ro" \
--volume="/etc/localtime:/etc/localtime:ro" \
--volume="winehome:/home/wineuser" \
--hostname="winecellar" \
--name="wine" \
$1

