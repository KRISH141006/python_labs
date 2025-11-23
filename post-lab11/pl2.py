from PIL import Image, ImageOps
import matplotlib.pyplot as plt

img = Image.open(r"E:\d_drive\sem_3\pwp\lab\MU.jpg")
padded_img = ImageOps.expand(img, border=50, fill="black")
padded_img.show()
