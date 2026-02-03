import cv2
import numpy as np

class BlockMatcher:
    def __init__(self, num_disparities=16, block_size=15):
        # num_disparities: Arama yapılacak piksel aralığı (16'nın katı olmalı)
        # block_size: Karşılaştırılacak pencere boyutu (tek sayı olmalı)
        self.stereo = cv2.StereoBM_create(numDisparities=num_disparities, blockSize=block_size)

    def compute_disparity(self, left_gray, right_gray):
        """İki görüntü arasındaki eşleşmeleri bulur ve fark haritasını döner."""
        disparity = self.stereo.compute(left_gray, right_gray)
        # Görüntülemek için normalize edilir
        return cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)