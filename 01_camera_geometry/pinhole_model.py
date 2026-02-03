import numpy as np

def project_point(X, Y, Z, f):
    x = (X * f) / Z
    y = (Y * f) / Z

    return x,y
X,Y,Z = 2, 1, 10
f = 800

x, y = project_point(X, Y, Z, f)

print(f"3D Nokta: ({X}, {Y}, {Z})")
print(f"2D Görüntü Noktası: ({x:.2f}, {y:.2f})")    # (x = fx/z) (y = fy/z)