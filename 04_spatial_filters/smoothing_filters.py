import cv2
import numpy as np

class PhysicsBasedSmoothing:
    def anisotropic_diffusion(self, image, iterations=10, delta_t=0.1, kappa=50):
        """Görüntüyü bir fiziksel difüzyon denklemiyle yumuşatır."""
        img = image.astype('float32')
        for i in range(iterations):
            dy, dx = np.gradient(img)
            # Difüzyon katsayısı (Kenarlarda akışı durdurur)
            c = np.exp(-(dx**2 + dy**2)/(kappa**2))
            img = img + delta_t * (np.gradient(c*dx)[1] + np.gradient(c*dy)[0])
        return np.clip(img, 0, 255).astype('uint8')