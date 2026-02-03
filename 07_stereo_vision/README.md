# 07 - Stereo Vision and Depth Estimation

İki kamera kullanarak 3D derinlik bilgisinin çıkarılması.

## Matematiksel Temeller
1. **Disparity (d):** Sol ve sağ görüntüdeki eşleşen piksellerin konum farkı ($x_{sol} - x_{sağ}$).
2. **Derinlik Formülü:** $Z = \frac{f \cdot B}{d}$
   - $f$: Focal length (Odak uzaklığı)
   - $B$: Baseline (Kamera arası mesafe)

## İçerik
- `block_matching.py`: Piksel bloklarını eşleştirme algoritmaları.
- `disparity_map.py`: Piksel bazlı fark haritası oluşturma.
- `depth_estimation.py`: Disparite verisini fiziksel uzaklığa dönüştürme.