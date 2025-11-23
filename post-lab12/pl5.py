import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

x = np.sin(2*np.pi*5*t)
x_rev = x[::-1]

plt.plot(t, x, label="Original")
plt.plot(t, x_rev, label="Reversed")
plt.legend()
plt.title("Time Reversal of Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
