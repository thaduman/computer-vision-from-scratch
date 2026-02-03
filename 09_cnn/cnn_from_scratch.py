import numpy as np

class SimpleCNNLayer:
    def __init__(self, num_filters, filter_size):
        # Filtreleri rastgele başlat (Xavier/He initialization basitleştirilmiş hali)
        # Boyut: (Filtre Sayısı, Filtre Yüksekliği, Filtre Genişliği)
        self.num_filters = num_filters
        self.filter_size = filter_size
        self.filters = np.random.randn(num_filters, filter_size, filter_size) / 9.0

    def iterate_regions(self, image):
        """
        Görüntü üzerinde filtre boyutunda pencereler gezdirir (Generator).
        """
        h, w = image.shape
        for i in range(h - self.filter_size + 1):
            for j in range(w - self.filter_size + 1):
                im_region = image[i:(i + self.filter_size), j:(j + self.filter_size)]
                yield im_region, i, j

    def forward(self, input_image):
        """
        Konvolüsyon işlemini gerçekleştirir.
        Girdi: 2D Görüntü (H, W)
        Çıktı: 3D Tensör (Num_Filters, H_out, W_out)
        """
        h, w = input_image.shape
        output_dim = (h - self.filter_size + 1)
        output = np.zeros((output_dim, output_dim, self.num_filters))

        for im_region, i, j in self.iterate_regions(input_image):
            # Matematiksel işlem: Z = (X * W) (Bias ihmal edildi)
            # Her filtre için çarpım ve toplam
            output[i, j] = np.sum(im_region * self.filters, axis=(1, 2))

        # ReLU Aktivasyonu: A = max(0, Z)
        return np.maximum(0, output)