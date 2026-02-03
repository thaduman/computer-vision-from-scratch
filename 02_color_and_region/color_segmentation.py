import cv2
import numpy as np

class color_segmenter:
    def __init__(self, lower_bound, upper_bound):
        self.lower = np.array(lower_bound)  # alt sınır
        self.upper = np.array(upper_bound)  # üst sınır

    def segment(self, frame):
        # görüntuyu hsv formatina ceviriyoruz (renk aralığına) (Hue, Saturation, Value)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #thresholding(matematiksel maskeleme)
        mask = cv2.inRange(hsv_frame, self.lower, self.upper)
        # orijinal görüntü üzerinde masekeyi uygulayalım
        result = cv2.bitwise_and(frame, frame, mask=mask)
        return mask, result
    
# Mavi rengi örnek olarak kullanalım:
lower_blue = [100, 150, 0]
upper_blue = [140, 255, 255]

segmenter = color_segmenter(lower_blue, upper_blue)



