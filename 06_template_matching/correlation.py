import cv2
import numpy as np

class CorrelationAnalyzer:
    def apply_correlation(self, image, template):
        # OpenCV'de filter2D aslında teknik olarak korelasyon yapar
        return cv2.filter2D(image, -1, template)

    def normalized_correlation(self, image, template):
        res = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
        return res