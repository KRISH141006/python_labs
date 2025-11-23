import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

x = np.sin(2*np.pi*10*t)
scaled = 3 * x

plt.plot(t, x, label="Original")
plt.plot(t, scaled, label="Scaled (×3)")
plt.legend()
plt.title("Amplitude Scaling")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
