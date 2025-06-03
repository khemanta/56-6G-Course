# Title: Massive MIMO and mmWave Simulation

# A6_massive_mimo_mmwave.ipynb
# Author: 5G/6G Learning Series
# Topic: Massive MIMO & mmWave Communications
##-----------------------------------------------------------------------------#

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set(style="whitegrid")
np.random.seed(42)

##-----------------------------------------------------------------------------#

# --- 1. Massive MIMO Capacity Simulation ---
def simulate_mimo_capacity(Nt, max_Nr, snr_db):
    snr_linear = 10 ** (snr_db / 10)
    num_antennas = np.arange(1, max_Nr+1, 5)
    capacity = []

    for Nr in num_antennas:
        H = (1 / np.sqrt(2)) * (np.random.randn(Nr, Nt) + 1j * np.random.randn(Nr, Nt))
        HH = H @ H.conj().T
        cap = np.log2(np.linalg.det(np.eye(Nr) + (snr_linear / Nt) * HH)).real
        capacity.append(cap)

    return num_antennas, capacity

Nt = 1
max_Nr = 100
snr_db = 10

nr_list, capacity_list = simulate_mimo_capacity(Nt, max_Nr, snr_db)

plt.figure(figsize=(10, 6))
plt.plot(nr_list, capacity_list, marker='o')
plt.title("📶 Massive MIMO: Capacity vs Number of Receive Antennas")
plt.xlabel("Number of Receive Antennas (Nr)")
plt.ylabel("Channel Capacity (bps/Hz)")
plt.grid(True)
plt.tight_layout()
plt.savefig("./figures/massive_mimo_capacity.png")
plt.show()


##-----------------------------------------------------------------------------#

# --- 2. mmWave Path Loss Comparison (Friis Model) ---
def fspl(frequency_ghz, distance_m):
    c = 3e8  # speed of light in m/s
    frequency_hz = frequency_ghz * 1e9
    wavelength = c / frequency_hz
    return 20 * np.log10(4 * np.pi * distance_m / wavelength)

frequencies = [2.4, 28, 60]  # GHz
distance = np.linspace(1, 200, 500)

plt.figure(figsize=(10, 6))
for f in frequencies:
    path_loss = fspl(f, distance)
    plt.plot(distance, path_loss, label=f'{f} GHz')

plt.title("📡 Free-Space Path Loss vs Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Path Loss (dB)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("./figures/mmwave_fspl_comparison.png")
plt.show()

##-----------------------------------------------------------------------------#

# --- 3. Beamwidth vs Antenna Elements ---
def beamwidth(num_elements):
    return 102 / num_elements  # Approximate formula

num_elements = np.arange(1, 129, 2)
beamwidth_deg = beamwidth(num_elements)

plt.figure(figsize=(10, 6))
plt.plot(num_elements, beamwidth_deg, marker='x', color='darkgreen')
plt.title("🎯 Beamwidth vs Number of Antenna Elements")
plt.xlabel("Number of Antenna Elements")
plt.ylabel("Beamwidth (degrees)")
plt.grid(True)
plt.tight_layout()
plt.savefig("./figures/beamwidth_vs_elements.png")
plt.show()

##-----------------------------------------------------------------------------#




