import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

x = np.sin(2*np.pi*5*t)
shift = 0.1
x_shifted = np.sin(2*np.pi*5*(t - shift))

plt.plot(t, x, label="Original")
plt.plot(t, x_shifted, label="Shifted (0.1 s)")
plt.legend()
plt.title("Time-Shifted Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
