import numpy as np
import matplotlib.pyplot as plt

fs = 500
t = np.arange(0, 2, 1/fs)

sine = np.sin(2*np.pi*5*t)
cosine = np.cos(2*np.pi*10*t)

product = sine * cosine

plt.plot(t, product)
plt.title("Product of 5 Hz Sine and 10 Hz Cosine")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
