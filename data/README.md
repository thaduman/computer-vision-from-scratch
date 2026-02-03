# Data Directory (Veri Klasörü)

Bu klasör, **Computer Vision From Scratch** projesindeki scriptlerin çalışması için gereken tüm test görsellerini, video dosyalarını, eğitilmiş modelleri ve veri setlerini barındırır.

Kodların hatasız çalışması için dosyalarınızı aşağıdaki yapıya uygun olarak düzenlemeniz önerilir.

---

## Önerilen Klasör Yapısı

Projenizin düzenli kalması için `data` klasörü içinde şu alt klasörleri oluşturabilirsiniz:

```text
data/
├── images/                  # Temel test görselleri (01-05 modülleri için)
│   ├── test_image.jpg       # Genel test resmi (Lenna, Cameraman vb.)
│   ├── coins.png            # Blob detection ve morfoloji testleri için
│   └── gradient.png         # Filtreleme testleri için
│
├── stereo/                  # Stereo Vision (07) için çiftli görüntüler
│   ├── left_img.png         # Sol kamera görüntüsü
│   └── right_img.png        # Sağ kamera görüntüsü (Rectified)
│
├── templates/               # Şablon Eşleme (06) için dosyalar
│   ├── main_scene.jpg       # Ana büyük resim
│   └── pattern.jpg          # İçinde aranacak küçük parça (template)
│
├── models/                  # Eğitilmiş Yapay Zeka Modelleri
│   ├── haarcascade_frontalface_default.xml  # (10) Yüz tespiti için XML
│   ├── svm_model.pkl        # (08) Kaydedilmiş SVM modeli
│   └── cnn_model.pth        # (09) PyTorch ile eğitilmiş CNN ağırlıkları
│
└── requirements.txt         # Proje bağımlılıklarını içeren dosya


Her modülün test edilebilmesi için ihtiyaç duyduğu veri tipleri aşağıdadır:
Modül,Gerekli Dosya,Açıklama
01-05 Basics,.jpg / .png,Standart görüntü işleme testleri için herhangi bir renkli veya gri resim.
06 Template,Ana Resim + Şablon,cv2.matchTemplate fonksiyonu için büyük bir resim ve o resimden kesilmiş küçük bir parça.
07 Stereo,Stereo Çifti (L/R),Derinlik haritası (Disparity Map) çıkarmak için Middlebury Stereo Dataset gibi kaynaklardan alınan sol/sağ görüntüler.
08 ML,Veri Seti,Özellik çıkarımı (HOG/LBP) eğitimi için sınıflandırılmış resimler.
09 CNN,MNIST / CIFAR-10,Genellikle torchvision kütüphanesi bu verileri otomatik indirir ve bu klasöre kaydeder.
10 Detection,.xml Dosyası,OpenCV Haar Cascade modelleri (OpenCV kurulumuyla gelir veya internetten indirilir).