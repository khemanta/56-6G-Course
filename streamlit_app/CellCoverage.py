
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="📶 Cell Coverage Visualizer", layout="wide")

st.title("📶 Signal Strength & Path Loss Visualizer")

st.markdown("""
This app simulates **signal attenuation** in wireless communication based on:
- 📡 **Free Space Path Loss (FSPL)**
- 🏙️ **Log-distance Path Loss Model**

Adjust the parameters to see how signal degrades with distance.
""")

# Sidebar Controls
st.sidebar.header("Simulation Parameters")

f = st.sidebar.slider("📡 Frequency (GHz)", 0.7, 6.0, 2.0, 0.1)
f_hz = f * 1e9  # Convert GHz to Hz

max_distance = st.sidebar.slider("📏 Max Distance (meters)", 10, 5000, 1000, 100)
d = np.linspace(1, max_distance, 1000)

n = st.sidebar.slider("🏙️ Path Loss Exponent (n)", 1.0, 6.0, 3.5, 0.1)

# FSPL Calculation
fspl = 20 * np.log10(d) + 20 * np.log10(f_hz) - 147.55

# Log-distance Path Loss
d0 = 1  # reference distance
pl_log = 20 * np.log10(d0) + 10 * n * np.log10(d/d0)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(d, fspl, label='Free Space Path Loss', linewidth=2)
ax.plot(d, pl_log, label=f'Log-distance Path Loss (n={n})', linestyle='--', linewidth=2)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Path Loss (dB)')
ax.set_title('Signal Path Loss vs Distance')
ax.grid(True)
ax.legend()

st.pyplot(fig)
