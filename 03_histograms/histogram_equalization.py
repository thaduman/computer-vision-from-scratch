import cv2
import numpy as np

class HistogramEqualizer:
    def apply_equalization(self, image):
        if len(image.shape) == 3:
            # Renkli görüntülerde sadece parlaklık kanalı (Y) eşitlenir.
            ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
            channels = list(cv2.split(ycrcb))
            channels[0] = cv2.equalizeHist(channels[0])
            result = cv2.merge(channels)
            return cv2.cvtColor(result, cv2.COLOR_YCrCb)
        else:
            return cv2.equalizeHist(image)
        