# Gaussian Splatting

Este repositorio implementa el método de **3D Gaussian Splatting** de [graphdeco-inria](https://github.com/graphdeco-inria/gaussian-splatting).

---

## 📥 Clonar el repositorio

Clonar el repositorio original junto con sus submódulos:

```bash
git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive
cd gaussian-splatting
```

## 🐳 Ejecución en contenedor Docker
1. Ir a la carpeta de docker/
2. Ejecutar contenedor

```bash
cd docker
./launch_bash.sh
```

## 📦 Instalación de dependencias
Dentro del contenedor, instalar los submódulos y librerías adicionales:

### Submódulos
```bash
cd submodules/diff-gaussian-rasterization
pip install .

cd ../fused-ssim
pip install .

cd ../simple-knn
pip install .

```

### Librerías extra
```bash
pip install plyfile
pip install opencv-python
pip install tqdm

```

## How to use this repository?
```bash
# 1. Convertir datos
python convert.py -s data/bottle/

# 2. Entrenar
python train.py -s data/bottle/

# 3. Renderizar resultados
python render.py -m output/f51dae7c-3

```
