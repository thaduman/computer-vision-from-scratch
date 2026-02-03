import cv2
import numpy as np
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

class ClassicalML:
    def __init__(self, model_type="SVM"):
        if model_type == "SVM":
            self.model = svm.SVC(kernel='linear', probability=True)
        elif model_type == "KNN":
            self.model = KNeighborsClassifier(n_neighbors=3)

    def extract_hog_features(self, image):
        """HOG (Histogram of Oriented Gradients) özniteliklerini çıkarır."""
        image_resized = cv2.resize(image, (64, 128))
        hog = cv2.HOGDescriptor()
        return hog.compute(image_resized).flatten()

    def train(self, features, labels):
        """Modeli eğitir."""
        self.model.fit(features, labels)

    def predict(self, feature):
        """Yeni bir görüntünün sınıfını tahmin eder."""
        return self.model.predict([feature])