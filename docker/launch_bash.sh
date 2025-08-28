#!/bin/bash

IMAGE_NAME="gaussian-splatting-cuda11"
CONTAINER_NAME="gaussian-splatting-container_v2"

LOCAL_DIR="/home/horte/Documents/horte/GitHub/gaussian-splatting"
CONTAINER_DIR="/root/gaussian-splatting"

echo "🛠️  Construyendo la imagen '$IMAGE_NAME'..."
docker build -t $IMAGE_NAME .

echo "🚀 Iniciando contenedor '$CONTAINER_NAME'..."
docker run -it \
    --cpus=14 \
    --runtime=nvidia \
    --gpus all \
    -v /dev/shm:/dev/shm \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --network="host" \
    --device /dev/dri:/dev/dri \
    --ipc="host" \
    --privileged \
    -e DISPLAY=$DISPLAY \
    --name $CONTAINER_NAME \
    -v "$LOCAL_DIR:$CONTAINER_DIR" \
    $IMAGE_NAME

    # --memory=11g \
    # --memory-swap=17g \
    # --shm-size=6g \
