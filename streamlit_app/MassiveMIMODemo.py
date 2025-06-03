# ✅ Instructions
#  - Save this as MassiveMIMODemo.py in your Streamlit app folder.
#  - Add this page using st.sidebar navigation or use multipage configuration.
#  - Ensure matplotlib and numpy are installed:

#   ```python
#   pip install streamlit matplotlib numpy

#   ```

##-----------------------------------------------------------------------------##

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Massive MIMO & mmWave Demo", layout="wide")

st.title("📶 Massive MIMO & mmWave Communication Simulator")

tab1, tab2, tab3 = st.tabs(["MIMO Capacity", "mmWave Path Loss", "Beamwidth"])

# -----------------------
# Tab 1: MIMO Capacity
# -----------------------
with tab1:
    st.subheader("📈 MIMO Channel Capacity Simulation")
    snr_db = st.slider("SNR (dB)", min_value=0, max_value=30, value=10)
    Nt = st.slider("Number of Transmit Antennas (Nt)", 1, 16, 1)
    max_Nr = st.slider("Max Number of Receive Antennas (Nr)", 10, 200, 100)

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

    x, y = simulate_mimo_capacity(Nt, max_Nr, snr_db)

    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title("Channel Capacity vs Number of Receive Antennas")
    ax.set_xlabel("Nr")
    ax.set_ylabel("Capacity (bps/Hz)")
    ax.grid(True)
    st.pyplot(fig)

# -----------------------
# Tab 2: mmWave Path Loss
# -----------------------
with tab2:
    st.subheader("📡 Path Loss over Distance for mmWave")
    distances = np.linspace(1, 200, 500)
    selected_freqs = st.multiselect("Select Frequencies (GHz):", [2.4, 28, 60], default=[2.4, 28, 60])

    def fspl(frequency_ghz, distance_m):
        c = 3e8
        wavelength = c / (frequency_ghz * 1e9)
        return 20 * np.log10(4 * np.pi * distance_m / wavelength)

    fig2, ax2 = plt.subplots()
    for f in selected_freqs:
        loss = fspl(f, distances)
        ax2.plot(distances, loss, label=f'{f} GHz')
    ax2.set_title("Free Space Path Loss")
    ax2.set_xlabel("Distance (m)")
    ax2.set_ylabel("Path Loss (dB)")
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)

# -----------------------
# Tab 3: Beamwidth
# -----------------------
with tab3:
    st.subheader("🎯 Beamwidth vs Antenna Elements")
    num_elems = np.arange(1, 129, 2)

    def beamwidth(n):
        return 102 / n

    widths = beamwidth(num_elems)

    fig3, ax3 = plt.subplots()
    ax3.plot(num_elems, widths, marker='x', color='darkgreen')
    ax3.set_title("Beamwidth vs Antenna Elements")
    ax3.set_xlabel("Number of Elements")
    ax3.set_ylabel("Beamwidth (degrees)")
    ax3.grid(True)
    st.pyplot(fig3)

##-----------------------------------------------------------------------------##    
