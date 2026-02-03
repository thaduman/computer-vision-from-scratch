import cv2
import numpy as np

class ImageSubtractor:
    def subtract_images(self, img1, img2):
        return cv2.subtract(img1, img2)

    def background_subtraction(self, frame, background):
        diff = cv2.absdiff(frame, background)
        # Gürültüyü temizlemek için eşikleme
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        return thresh

    def morph_gradient_manual(self, image, kernel_size=(3,3)):
        kernel = np.ones(kernel_size, np.uint8)
        dilated = cv2.dilate(image, kernel)
        eroded = cv2.erode(image, kernel)
        return cv2.subtract(dilated, eroded)