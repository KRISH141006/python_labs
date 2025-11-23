from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"E:\d_drive\sem_3\pwp\lab\MU.jpg")
img_np = np.array(img)

R = img_np[:, :, 0]
G = img_np[:, :, 1]
B = img_np[:, :, 2]

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(R, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(G, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(B, cmap="gray")
plt.axis("off")

plt.show()
