# Computer Vision from Scratch

A progressive, ground-up implementation of computer vision algorithms — from camera geometry and pixel operations to CNNs built with NumPy and PyTorch. Every module is grounded in the underlying mathematics before moving to code.

Built with **Python · OpenCV · NumPy · PyTorch · Scikit-learn**

---

## Why this project exists

Most computer vision courses hand you high-level library calls without explaining what happens underneath. This project takes the opposite approach: each topic starts from the mathematical foundation, then implements it step by step in Python — so the how and the why are always connected.

---

## Curriculum

| # | Module | Topics covered |
|---|--------|---------------|
| 01 | **Camera geometry** | Pinhole camera model, 3D→2D projection, distance estimation |
| 02 | **Color & region** | HSV color segmentation, area calculation |
| 03 | **Histograms** | Histogram analysis, equalization techniques |
| 04 | **Spatial filters** | Convolution from scratch, Gaussian/Box filters, edge sharpening |
| 05 | **Pixel operations** | Image subtraction, Gamma & Log transformations |
| 06 | **Template matching** | Correlation, similarity metrics (SSD, NCC) |
| 07 | **Stereo vision** | Dual-camera depth estimation, disparity maps |
| 08 | **Learning-based methods** | HOG + SVM pipeline, learnable filters |
| 09 | **CNN** | Convolutional Neural Networks built from scratch in NumPy, then in PyTorch |
| 10 | **Object detection** | Haar Cascades and HOG-based detection |

---

## Getting started

**Requirements**

```
Python 3.8+
opencv-python
numpy
torch
scikit-learn
```

**Install dependencies**

```bash
pip install opencv-python numpy torch scikit-learn
```

**Run a module**

Each module is self-contained. Navigate into any folder and run its script:

```bash
cd 04_spatial_filters
python spatial_filters.py
```

Sample images are provided in the `data/` folder.

---

## Stack

| Layer | Tools |
|-------|-------|
| Core language | Python 3.8+ |
| Image processing | OpenCV, PIL |
| Numerical computing | NumPy |
| Deep learning | PyTorch |
| Classical ML | Scikit-learn (SVM, HOG) |

---

## Key highlights

- **CNN implemented in pure NumPy** — forward pass, convolution, and pooling without any deep learning framework
- **Stereo vision & depth estimation** — dual-camera geometry implemented from the projection equations
- **Full classical → deep learning progression** — from pixel math to a trained neural network in one repo
- **Math-first approach** — every module explains the underlying equations before the implementation

---

## Author

**Muhammet Taha Duman**
Computer Engineering — İnönü University

[LinkedIn](https://www.linkedin.com/in/muhammet-taha-duman-24834222a/) · [GitHub](https://github.com/thaduman)
