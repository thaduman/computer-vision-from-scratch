import cv2
import numpy as np

class SimilarityMetrics:
    def compute_sad(self, patch1, patch2):
        return np.sum(np.abs(patch1.astype("float") - patch2.astype("float")))

    def compute_ssd(self, patch1, patch2):
        """Sum of Squared Differences (SSD)"""
        return np.sum((patch1.astype("float") - patch2.astype("float")) ** 2)

    def compute_cosine_similarity(self, patch1, patch2):
        """Vektör tabanlı kosinüs benzerliği."""
        p1 = patch1.flatten()
        p2 = patch2.flatten()
        return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))