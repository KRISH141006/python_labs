# 1

import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
# Load audio file
audio, sample_rate = sf.read('audio.wav')
# Create time axis
time = np.arange(0, len(audio)) / sample_rate
# Plot audio signal
plt.plot(time, audio)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
