FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# setup
RUN apt-get update && apt-get install -y \
    wget curl git bzip2 unzip ffmpeg zip \
    build-essential cmake ninja-build \
    libgl1-mesa-dev libx11-dev libxi-dev libxmu-dev \
    libglu1-mesa-dev libglew-dev libomp-dev \
    qtbase5-dev && \
    apt-get clean

# Miniforge (conda-forge first)
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O /tmp/mf.sh && \
    bash /tmp/mf.sh -b -p $CONDA_DIR && rm /tmp/mf.sh && \
    conda config --set channel_priority strict && \
    conda config --remove-key channels || true && \
    conda config --add channels conda-forge

# env
RUN conda create -n gaussian-splatting -y python=3.8

# activar en shells interactivos
RUN echo "source activate gaussian-splatting" >> ~/.bashrc

# PyTorch cu118 + ninja (vía pip como tienes)
RUN /bin/bash -c "source $CONDA_DIR/bin/activate gaussian-splatting && \
    pip install --upgrade pip && \
    pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 ninja \
        --extra-index-url https://download.pytorch.org/whl/cu118"

# cuda archs
ENV TCNN_CUDA_ARCHITECTURES="70,75,80,86,89"

# tiny-cuda-nn
RUN /bin/bash -c "source $CONDA_DIR/bin/activate gaussian-splatting && \
    pip install git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch"

# COLMAP desde conda-forge
RUN /bin/bash -c "source $CONDA_DIR/bin/activate gaussian-splatting && \
    conda install -y -c conda-forge \
      colmap=3.8 \
      boost eigen gflags glog \
      freeimage suitesparse glew qt libpng libjpeg-turbo \
      cgal"

SHELL ["/bin/bash", "-c"]
CMD ["bash", "-l"]
