# 05 - Image Subtraction and Intensity Transforms

Bu bölüm, pikseller arasındaki farkları hesaplama ve yoğunluk (intensity) değerlerini matematiksel fonksiyonlarla dönüştürme tekniklerini içerir.

## Matematiksel Formüller
1. **Görüntü Çıkarma:** $g(x,y) = f(x,y) - h(x,y)$
2. **Gamma Dönüşümü:** $s = c \cdot r^\gamma$
3. **Log Dönüşümü:** $s = c \cdot \log(1+r)$

## İçerik
- `image_subtraction.py`: Hareket algılama ve gradyan analizi.
- `intensity_transforms.py`: Gamma düzeltme ve logaritmik kontrast artırma.