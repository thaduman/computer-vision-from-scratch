import numpy as np

class LearningFilter:
    def __init__(self, kernel_size=3):
        # Başlangıçta rastgele katsayılara sahip bir kernel
        self.kernel = np.random.randn(kernel_size, kernel_size)
        self.learning_rate = 0.01

    def forward(self, image_patch):
        return np.sum(image_patch * self.kernel)

    def update_weights(self, image_patch, error):
        # Gradyan = hata * girdi
        gradient = error * image_patch
        self.kernel -= self.learning_rate * gradient

    def get_learned_kernel(self):
        return self.kernel