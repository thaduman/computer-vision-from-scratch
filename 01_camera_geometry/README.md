Bu bölüm, 3D dünyadaki bir noktanın kamera düzlemine nasıl düştüğünü ve mesafelerin nasıl tahmin edildiğini kapsar.

Pinhole Model: 3D'den 2D'ye izdüşüm.

Size & Distance Estimation: Görüntüdeki boyuttan mesafe tahmini.

Pinhole Kamera Modeli: 
Bir nesnenin gerçek dünyadaki koordinatları (X, Y, Z) ve odak uzaklığı f ise, görüntü düzlemindeki (x, y) koordinatları benzer üçgenler prensibiyle hesaplanır:
x = f*X/Z ve y = f*Y/Z

Mesafe Tahmini:
Bir nesnenin gerçek yüksekliği H ve görüntüdeki piksel yüksekliği h biliniyorsa, kameraya olan uzaklık Z şu formülle bulunur: 
Z = f*H/h