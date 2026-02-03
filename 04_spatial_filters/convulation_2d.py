import cv2
import numpy as np

class FrequencyDomainFilter:
    def fft_convolution(self, image, kernel):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        f_image = np.fft.fft2(gray)
        f_kernel = np.fft.fft2(kernel, s=gray.shape)

        f_result = f_image * f_kernel

        img_back = np.fft.ifft2(f_result)
        return np.abs(img_back).astype(np.uint8)
    
    