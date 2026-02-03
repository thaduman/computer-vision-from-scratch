import cv2
import numpy as np

class IntensityTransformer:
    def log_transform(self, image):
        c = 255 / np.log(1 + np.max(image))
        log_image = c * (np.log(image + 1))
        return np.array(log_image, dtype=np.uint8)

    def gamma_correction(self, image, gamma=1.0):
        # Piksel değerlerini 0-1 arasına normalize et
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 
                          for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(image, table)

    def image_negative(self, image):
        return 255 - image