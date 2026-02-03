import cv2
import numpy as np

class Sharpening:
    def high_boost_filter(self, image, k=1.5):
        blurred = cv2.GaussianBlur(image, (3,3), 0) #alçak geçiren filtre (blur)
        mask = cv2.subtract(image, blurred) # maske oluştur (orijinal - blur)
        sharpened = cv2.addWeighted(image, 1.0, mask, k, 0) # orijinal üzerine maskeyi ekle (k katı kadar)
        return sharpened