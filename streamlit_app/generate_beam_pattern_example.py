import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 8  # Number of antennas
d = 0.5  # Antenna spacing in wavelengths
theta = np.linspace(-90, 90, 1000)
theta_rad = np.deg2rad(theta)
k = 2 * np.pi  # Wave number

# Beamforming weights (steering angle at 30 degrees)
steering_angle = 30
steering_rad = np.deg2rad(steering_angle)
weights = np.exp(1j * k * d * np.arange(N) * np.sin(steering_rad))

# Array factor
AF = np.zeros_like(theta_rad, dtype=complex)
for n in range(N):
    AF += weights[n] * np.exp(1j * k * d * n * np.sin(theta_rad))

AF_magnitude = np.abs(AF) / np.max(np.abs(AF))

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(theta, 20 * np.log10(AF_magnitude))
plt.title(f'Beam Pattern for Steering Angle = {steering_angle}°')
plt.xlabel('Angle (degrees)')
plt.ylabel('Normalized Gain (dB)')
plt.grid(True)
plt.ylim(-40, 0)
plt.tight_layout()
plt.savefig("../figures/beam_pattern_example.png")
plt.show()
