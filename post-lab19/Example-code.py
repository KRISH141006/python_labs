import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, lti ,bode

def analyze_z_transfer_function(num, den):
    # Create a Transfer Function object
    system = TransferFunction(num, den)

    # Get the poles and zeros
    zeros = system.zeros
    poles = system.poles
    print("Zeros:", zeros)
    print("Poles:", poles)
    # Stability Analysis
    stable = all(np.abs(pole) < 1 for pole in poles)
    print("Stability:", "Stable" if stable else "Unstable")

    # Causality Analysis
    causal = all(num[i] == 0 for i in range(len(num) - 1) if num[i + 1] == 0)
    print("Causality:", "Causal" if causal else "Non-Causal")
    # Time Invariance Analysis
    time_invariant = True  # For Z-transforms, generally time-invariant if system defined properly
    print("Time Invariance:", "Time Invariant" if time_invariant else "Time Variant")
    # Bode plot (magnitude and phase)
    w, mag, phase = bode(system)
    # Plot Bode plot
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.semilogx(w, mag)    # Bode magnitude plot
    plt.title('Bode Magnitude Plot')
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('Magnitude [dB]')
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.semilogx(w, phase)   # Bode phase plot
    plt.title('Bode Phase Plot')
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('Phase [degrees]')
    plt.grid()
    plt.tight_layout()
    plt.show()

# Example: Analyzing a specific system H(z) = (z^2 + 0.5)/(z^2 - 1.5z + 0.5)
num = [1, 0.5]  # Numerator coefficients
den = [1, -1.5, 0.5]  # Denominator coefficients
analyze_z_transfer_function(num, den)
