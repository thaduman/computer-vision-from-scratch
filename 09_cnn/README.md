# 09 - Convolutional Neural Networks (CNN)

Bu bölüm, manuel filtreleme işlemlerinden (Sobel, Gaussian) öğrenilebilir filtrelere geçişi temsil eder. Modern yapay zekanın temel taşıdır.

## Mimari
1. **Convolution Layer:** Görüntüden öznitelik (feature map) çıkarır.
2. **ReLU:** Doğrusallığı kırar (Non-linearity), modeli akıllandırır.
3. **Pooling:** Görüntü boyutunu küçültür, işlem yükünü azaltır.
4. **Fully Connected:** Çıkarılan özniteliklere göre karar verir.

## İçerik
- `cnn_from_scratch.py`: Kütüphane kullanmadan numpy ile konvolüsyon mantığı.
- `cnn_with_pytorch.py`: PyTorch kullanarak endüstri standardı bir model tanımlama.