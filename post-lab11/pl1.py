from PIL import Image
import numpy as np

img = Image.open(r"E:\d_drive\sem_3\pwp\lab\MU.jpg")
img_np = np.array(img)

width, height = img.size
print("Dimensions:", width, "x", height)
print("Shape:", img_np.shape)

blue_channel = img_np[:, :, 2]
print("Min pixel value in Blue channel:", blue_channel.min())
