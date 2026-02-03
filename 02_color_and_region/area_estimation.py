class AreaEstimatior:
    def __init__(self, focal_length):
        self.f = focal_length

    def estimate_real_area(self, pixel_area, distance):
        # A = a*(Z/f)^2 formülü uygulanır (A = gerçek dünyadaki alanı(m^2), a = görüntüdeki alanı(piksel^2)) (Z = distance)
        real_area = pixel_area * (distance / self.f)**2
        return real_area
    
estimator = AreaEstimatior(focal_length = 800)
distance_to_obj = 5.0 #Metre
p_area = 5000 #piksel ^2

real_size = estimator.estimate_real_area(p_area, distance_to_obj)
print(f"Nesnenin gerçek dünyadaki alanı: {real_size:.4f} m^2'dir.")

        