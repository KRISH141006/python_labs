import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def autocorr(x):
    return np.correlate(x, x, mode='full')

def crosscorr(x, y):
    return np.correlate(x, y, mode='full')

fs1, clean = read("clean_audio.wav")
fs2, noisy = read("noisy_audio.wav")
fs3, periodic = read("periodic_audio.wav")

clean = clean.astype(float)
noisy = noisy.astype(float)
periodic = periodic.astype(float)

ac_clean = autocorr(clean)
ac_noisy = autocorr(noisy)
ac_periodic = autocorr(periodic)

cc_clean_noisy = crosscorr(clean, noisy)
cc_clean_periodic = crosscorr(clean, periodic)

plt.figure(figsize=(14, 12))

plt.subplot(3, 2, 1)
plt.plot(ac_clean)
plt.title("Autocorrelation - Clean Audio")

plt.subplot(3, 2, 2)
plt.plot(ac_noisy)
plt.title("Autocorrelation - Noisy Audio")

plt.subplot(3, 2, 3)
plt.plot(ac_periodic)
plt.title("Autocorrelation - Periodic Audio")

plt.subplot(3, 2, 4)
plt.plot(cc_clean_noisy)
plt.title("Cross-correlation: Clean vs Noisy")

plt.subplot(3, 2, 5)
plt.plot(cc_clean_periodic)
plt.title("Cross-correlation: Clean vs Periodic")

plt.tight_layout()
plt.show()
