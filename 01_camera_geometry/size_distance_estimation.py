def estimate_distance(f, real_height, image_height):
    # nesnenin kameraya olan uzaklığını tahmin eder

    Z = f * real_height / image_height # (Z = f*H/h)
    return Z

f = 800  # piksel
H = 1.7 # Metre
h = 170 # piksel

distance = estimate_distance(f, H, h)
print(f"Tahmini uzaklık: {distance:.2f} metre")