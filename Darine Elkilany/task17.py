import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

# Settings
height, width = 512, 512   # smaller for quick testing
salt_pepper_density = 0.2
fixed_window = 3
adaptive_max_window = 7

# --- Create synthetic test image ---
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
xx, yy = np.meshgrid(x, y)
base = (0.6 * np.exp(-((xx-0.3)**2 + (yy-0.4)**2)/0.02) +
        0.4 * np.exp(-((xx-0.7)**2 + (yy-0.7)**2)/0.04) + 0.2*xx).astype(np.float32)
base = (255 * (base - base.min()) / (base.max() - base.min())).astype(np.uint8)

# Add salt-and-pepper noise
rng = np.random.default_rng(42)
noisy = base.copy()
num_corrupted = int(salt_pepper_density * height * width)
coords = rng.choice(height*width, size=num_corrupted, replace=False)
vals = rng.choice([0, 255], size=num_corrupted)
flat = noisy.ravel()
flat[coords] = vals
noisy = flat.reshape((height, width))

# --- Standard Median Filter (OpenCV) ---
t0 = time.perf_counter()
median_std = cv2.medianBlur(noisy, fixed_window)
t1 = time.perf_counter()
time_std = t1 - t0
print(f"Standard median ({fixed_window}x{fixed_window}) time: {time_std:.3f} s")

# --- Adaptive Median Filter ---
def adaptive_median_filter(img, max_window=7):
    output = img.copy()
    m, n = img.shape
    for i in range(m):
        for j in range(n):
            window_size = 3
            while True:
                k = window_size // 2
                i_min, i_max = max(i-k, 0), min(i+k+1, m)
                j_min, j_max = max(j-k, 0), min(j+k+1, n)
                region = img[i_min:i_max, j_min:j_max]
                Zmed = np.median(region)
                Zmin, Zmax = region.min(), region.max()
                A1, A2 = Zmed - Zmin, Zmed - Zmax
                if A1 > 0 and A2 < 0:
                    if img[i, j] > Zmin and img[i, j] < Zmax:
                        output[i, j] = img[i, j]
                    else:
                        output[i, j] = Zmed
                    break
                else:
                    window_size += 2
                    if window_size > max_window:
                        output[i, j] = Zmed
                        break
    return output.astype(np.uint8)

t0 = time.perf_counter()
adaptive_out = adaptive_median_filter(noisy, max_window=adaptive_max_window)
t1 = time.perf_counter()
time_adaptive = t1 - t0
print(f"Adaptive median (max {adaptive_max_window}x{adaptive_max_window}) time: {time_adaptive:.3f} s")

# --- Show results ---
fig, axes = plt.subplots(1, 3, figsize=(12,4))
axes[0].imshow(noisy, cmap='gray'); axes[0].set_title("Noisy")
axes[1].imshow(median_std, cmap='gray'); axes[1].set_title(f"Standard Median {fixed_window}x{fixed_window}")
axes[2].imshow(adaptive_out, cmap='gray'); axes[2].set_title(f"Adaptive Median (max {adaptive_max_window})")
for ax in axes: ax.axis("off")
plt.tight_layout()
plt.show()

print(f"\nSummary: Adaptive filter is {time_adaptive/time_std:.2f}× slower than standard median.")

#i didn't know how to do it ..so i used chatgpt