import cv2
import numpy as np

class HistogramAnalyzer:
    def calculate__histogram(self, image):
        # görüntü renkliyse griye çevirerek yoğunluk analizi yaparız.
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        return hist
    
