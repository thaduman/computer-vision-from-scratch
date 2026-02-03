import cv2
import numpy as np

class HistogramMatcher:
    def match(self, source, reference):
        # Kaynak ve referansın kanallarını eşleştirir
        matched = np.zeros_like(source)
        for i in range(source.shape[2]): # Her renk kanalı (B, G, R) için
            src_values, src_unique_indices, src_counts = np.unique(source[:,:,i], return_inverse=True, return_counts=True)
            ref_values, ref_counts = np.unique(reference[:,:,i], return_counts=True)

            src_quantiles = np.cumsum(src_counts).astype(np.float64) / source[:,:,i].size
            ref_quantiles = np.cumsum(ref_counts).astype(np.float64) / reference[:,:,i].size

            interp_values = np.interp(src_quantiles, ref_quantiles, ref_values)
            matched[:,:,i] = interp_values[src_unique_indices].reshape(source[:,:,i].shape)
        return matched.astype(np.uint8)