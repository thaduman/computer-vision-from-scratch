import cv2
import numpy as np

class DisparityProcessor:
    def apply_sgbm(self, left_img, right_img):
        window_size = 3
        left_matcher = cv2.StereoSGBM_create(
            minDisparity=0,
            numDisparities=16*5,  # Max arama mesafesi
            blockSize=window_size,
            P1=8 * 3 * window_size**2,
            P2=32 * 3 * window_size**2,
            disp12MaxDiff=1,
            uniquenessRatio=15,
            speckleWindowSize=0,
            speckleRange=2,
            preFilterCap=63,
            mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
        )
        disparity = left_matcher.compute(left_img, right_img).astype(np.float32) / 16.0
        return disparity