import torch
import torch.nn as nn
import torch.nn.functional as F

class ModernCNN(nn.Module):
    def __init__(self):
        super(ModernCNN, self).__init__()
        # 1. Konvolüsyon Katmanı: 1 kanal (Gri) giriş, 32 kanal çıkış, 3x3 kernel
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3)
        # 2. Konvolüsyon Katmanı: 32 kanal giriş, 64 kanal çıkış
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3)
        
        # Boyut hesabı giriş görüntüsüne göre değişir (Burada örnek 28x28 MNIST varsayıldı)
        # 28 -> conv1(3x3) -> 26 -> pool(2x2) -> 13 -> conv2(3x3) -> 11 -> pool(2x2) -> 5
        self.fc1 = nn.Linear(in_features=64 * 5 * 5, out_features=128)
        self.fc2 = nn.Linear(in_features=128, out_features=10) 

    def forward(self, x):
        # x: (Batch_Size, 1, 28, 28)
        
        # Katman 1: Conv -> ReLU -> MaxPool
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2)
        
        # Katman 2: Conv -> ReLU -> MaxPool
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2)
        
        # Flatten: Matrisi vektöre çevir
        x = torch.flatten(x, 1)
        
        # Sınıflandırma (Yapay Sinir Ağı kısmı)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        
        # Softmax (Olasılık Dağılımı): P(y|x)
        output = F.log_softmax(x, dim=1)
        return output