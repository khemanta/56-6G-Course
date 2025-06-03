import numpy as np
import matplotlib.pyplot as plt

def generate_16qam_symbols(N):
    bits = np.random.randint(0, 2, (N, 4))
    real = 2 * (2 * bits[:, 0] + bits[:, 1]) - 3
    imag = 2 * (2 * bits[:, 2] + bits[:, 3]) - 3
    return real + 1j * imag

num_symbols = 500
noise_std = 0.3

symbols = generate_16qam_symbols(num_symbols)
noise = noise_std * (np.random.randn(num_symbols) + 1j * np.random.randn(num_symbols))
received = symbols + noise

plt.figure(figsize=(6, 6))
plt.scatter(received.real, received.imag, s=10, alpha=0.7, color='blue')
plt.title("16-QAM Constellation with Gaussian Noise")
plt.xlabel("In-Phase")
plt.ylabel("Quadrature")
plt.grid(True)
plt.axis("equal")
plt.tight_layout()

plt.savefig("../figures/modulation_constellation_example.png")
