
# ✅ Features:
#  - Adjustable SNR, Cyclic Prefix, and Channel Taps.
#  - Visual comparison: Received symbols vs Equalized symbols.
#  - Uses Least Squares Estimation for channel response.

# Channel Estimation and Equalization

# This notebook explores basic channel models, estimation, and equalization techniques commonly used
# in wireless communication systems, especially in OFDM systems like 4G/5G.


# 📦 Imports
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft

np.random.seed(42)

# 📡 Simulate Transmitted OFDM Signal

# Parameters
N = 64  # OFDM subcarriers
cp_len = 16  # Cyclic prefix length

# QPSK modulation (generate symbols from bits)
data_bits = np.random.randint(0, 2, N * 2)
symbols = (2 * data_bits[0::2] - 1) + 1j * (2 * data_bits[1::2] - 1)

# IFFT to generate time domain signal
ofdm_signal = ifft(symbols)
ofdm_cp = np.concatenate([ofdm_signal[-cp_len:], ofdm_signal])

# 🌊 Channel with Multipath Fading

# Define a simple multipath channel
channel_impulse = np.array([1, 0.5 + 0.3j, 0.2])
channel_output = np.convolve(ofdm_cp, channel_impulse)

# Add complex Gaussian noise
noise = (np.random.randn(len(channel_output)) + 1j * np.random.randn(len(channel_output))) * 0.05
received_signal = channel_output + noise

# 📥 Receiver: Remove Cyclic Prefix and Apply FFT

received_cp_removed = received_signal[cp_len:cp_len + N]
received_freq = fft(received_cp_removed)

# 🔍 Channel Estimation using LS Estimator

# Assume known transmitted symbols (ideal pilot-based LS estimation)
H_est = received_freq / symbols  # Least Squares estimate of the channel

# Equalize
equalized_symbols = received_freq / H_est

# 📊 Visualization

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(np.real(received_freq), np.imag(received_freq), color='red')
plt.title("Received Symbols (Frequency Domain)")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(np.real(equalized_symbols), np.imag(equalized_symbols), color='green')
plt.title("Equalized Symbols After LS Channel Estimation")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid(True)

plt.tight_layout()
plt.savefig("../figures/equalized_constellation.png")
plt.show()
