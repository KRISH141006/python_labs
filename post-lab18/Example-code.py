# # 1

# import numpy as np
# # Define two input signals
# x = [1, 2, 3, 4]
# h = [1, 0, -1]
# # Perform linear convolution using numpy
# linear_conv = np.convolve(x, h)
# print("Linear Convolution: ", linear_conv)


# # 2

# import numpy as np

# # Define two input signals
# x = [1, 2, 3, 4]
# h = [1, 0, -1]

# # Determine the length for circular convolution
# N = max(len(x), len(h))
# # Zero-pad the shorter sequence to match the length of the longer one
# x_padded = np.pad(x, (0, N - len(x)), mode='constant')
# h_padded = np.pad(h, (0, N - len(h)), mode='constant')
# # Perform circular convolution using FFT
# X_fft = np.fft.fft(x_padded)
# H_fft = np.fft.fft(h_padded)
# circular_conv = np.fft.ifft(X_fft * H_fft)
# # Only the real part is considered (since the imaginary part should be zero)
# circular_conv = np.real(circular_conv)
# print("Circular Convolution: ", circular_conv)

# # 3

# import numpy as np
# import matplotlib.pyplot as plt

# # Define two signals
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 4, 5, 6])

# # Perform cross-correlation using numpy
# cross_corr = np.correlate(x, y, mode='full')

# # Plot cross-correlation
# plt.stem(cross_corr)
# plt.title('Cross-Correlation')
# plt.show()

# 4

import numpy as np
import matplotlib.pyplot as plt

# Define a signal
x = np.array([1, 2, 3, 4, 5])
# Perform autocorrelation using numpy
auto_corr = np.correlate(x, x, mode='full')
# Plot autocorrelation
plt.stem(auto_corr)
plt.title('Autocorrelation')
plt.show()


