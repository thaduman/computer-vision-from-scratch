# 08 - Classical ML and Learning Filters

Bu bölüm, kural tabanlı görüntü işlemeden veri tabanlı öğrenme yöntemlerine geçişi kapsar.

## Teknik Detaylar
1. **Feature Extraction:** Görüntüden HOG veya LBP gibi ayırt edici vektörlerin çıkarılması.
2. **Classification:** SVM veya KNN gibi algoritmalarla nesne tanıma.
3. **Weight Update:** Filtre katsayılarının gradyan inişi (gradient descent) ile öğrenilmesi.

## İçerik
- `classical_ml.py`: HOG tabanlı SVM/KNN sınıflandırma süreçleri.
- `learning_filters.py`: Öğrenilebilir kernel matrisleri ve ağırlık güncelleme mantığı.