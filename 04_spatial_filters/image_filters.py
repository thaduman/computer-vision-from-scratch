import cv2
import numpy as np

class ImageFilter:
    def apply_bilateral(self, image, d=9, color_treshold=75, space_radius=75):
        return cv2.bilateralFilter(image, d, color_treshold, space_radius)
    def apply_clahe(self, image):
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        l = clahe.apply(l)
        return cv2.cvtColor(cv2.merge([l, a, b]), cv2.COLOR_LAB2BGR)
    
