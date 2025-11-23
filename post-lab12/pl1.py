import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

s1 = np.sin(2*np.pi*5*t)
s2 = np.sin(2*np.pi*10*t)
s = s1 + s2

plt.plot(t, s)
plt.title("Sum of 5 Hz and 10 Hz Sine Waves")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
