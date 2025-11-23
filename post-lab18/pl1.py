import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import fftconvolve

# Load audio
fs, audio = wavfile.read("audio.wav")
audio = audio.astype(float)

# Load impulse response
fs_ir, impulse = wavfile.read("impulse.wav")
impulse = impulse.astype(float)

# Make sure sample rates match
if fs != fs_ir:
    raise ValueError("Sample rates do not match!")

# Linear convolution
linear_conv = np.convolve(audio, impulse, mode='full')

# Circular convolution (using FFT)
N = len(audio) + len(impulse) - 1
circular_conv = np.fft.ifft(np.fft.fft(audio, N) * np.fft.fft(impulse, N)).real

# Plot comparison
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(audio)
plt.title("Original Audio Signal")

plt.subplot(3, 1, 2)
plt.plot(linear_conv)
plt.title("Linear Convolution Result")

plt.subplot(3, 1, 3)
plt.plot(circular_conv)
plt.title("Circular Convolution Result")

plt.tight_layout()
plt.show()
