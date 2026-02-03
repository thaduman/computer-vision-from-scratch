import cv2
import numpy as np

class DepthEstimator:
    def __init__(self, focal_length, baseline):
        self.f = focal_length
        self.B = baseline

    def estimate_depth(self, disparity):
        # Disparite 0 ise derinlik sonsuzdur
        depth = np.zeros_like(disparity, dtype=np.float32)
        mask = disparity > 0
        depth[mask] = (self.f * self.B) / disparity[mask]
        return depth