# Gaussian Splatting

Official implementation of the **3D Gaussian Splatting** method from [graphdeco-inria](https://github.com/graphdeco-inria/gaussian-splatting).  
This repository allows you to train, render, and experiment with 3D scenes from multi-view datasets.

---

## 📥 Clone the repository

Clone the original repository:

```bash
git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive
cd gaussian-splatting
```

## 🐳 Run with Docker
1. Go to the docker/ folder:
2. Launch the container:

```bash
cd docker
./launch_bash.sh
```
This will open a terminal inside the container with CUDA and base dependencies ready.

## 📦 Install dependencies
Inside the container, install the submodules and extra Python libraries.

### Submodules
```bash
cd submodules/diff-gaussian-rasterization
pip install .

cd ../fused-ssim
pip install .

cd ../simple-knn
pip install .

```

### Libraries
```bash
pip install plyfile
pip install opencv-python
pip install tqdm

```

## How to use this repository?
Once dependencies are installed, you can run the following commands:
```bash
# 1. Convert dataset (point cloud generation)
python convert.py -s data/bottle/

# 2. Train the model
python train.py -s data/bottle/

# 3. Render results from a trained model
python render.py -m output/f51dae7c-3

```

## 📂 Folder structure for data
```
data/<location>/
|---input
    |---<image 0>
    |---<image 1>
    |---...
```

