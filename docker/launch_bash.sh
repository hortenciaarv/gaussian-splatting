#!/bin/bash
set -e

IMAGE_NAME="gaussian-splatting-cuda11"
CONTAINER_NAME="gaussian-splatting-container"

LOCAL_DIR="/home/alumno/horte/gaussian-splatting"
CONTAINER_DIR="/root/gaussian-splatting"

echo "🛠️  Construyendo la imagen '$IMAGE_NAME'..."
docker build -t $IMAGE_NAME .

echo "🚀 Iniciando contenedor '$CONTAINER_NAME' (X11 real + OpenGL)..."
docker run -it \
  --cpus=64 \
  --runtime=nvidia --gpus all \
  --network=host \
  --ipc=host \
  --privileged \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -e NVIDIA_DRIVER_CAPABILITIES=all,compute,utility,video,graphics \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v /dev/shm:/dev/shm \
  --device /dev/dri:/dev/dri \
  -v "$LOCAL_DIR:$CONTAINER_DIR" \
  --name $CONTAINER_NAME \
  $IMAGE_NAME
