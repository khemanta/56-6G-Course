# 📥  BeamPatternVisualizer.py

# This file contains the complete Streamlit code for visualizing beamforming patterns with user-controlled inputs like:

# - Number of antennas
# - Antenna spacing
# - Beam steering angle
# - Type of beamforming (Analog / Digital / Hybrid)

# You can run it locally using:

```
# streamlit run BeamPatternVisualizer.py

```

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Beam Pattern Visualizer", layout="wide")

st.title("📡 Beam Pattern Visualizer")
st.markdown("Explore beam patterns for antenna arrays with different beamforming strategies.")

# Parameters
N = st.slider("Number of Antennas", min_value=2, max_value=32, value=8, step=1)
d_lambda = st.slider("Element Spacing (in λ)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
theta_steer_deg = st.slider("Steering Angle (degrees)", min_value=-90, max_value=90, value=0)
beamforming_type = st.selectbox("Beamforming Type", ["Analog", "Digital", "Hybrid"])

# Steering vector computation
def array_factor(N, d, theta_steer, theta_range):
    k = 2 * np.pi  # assume λ = 1
    n = np.arange(N)
    af = np.zeros_like(theta_range, dtype=complex)
    for i, theta in enumerate(theta_range):
        af[i] = np.sum(np.exp(1j * k * d * n * (np.sin(np.radians(theta)) - np.sin(np.radians(theta_steer)))))
    return np.abs(af) / N

theta = np.linspace(-90, 90, 1000)
af = array_factor(N, d_lambda, theta_steer_deg, theta)

# Plotting
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(theta, 20 * np.log10(np.maximum(af, 1e-6)))
ax.set_title(f"{beamforming_type} Beam Pattern (N={N}, d={d_lambda}λ, θₛ={theta_steer_deg}°)")
ax.set_xlabel("Angle (degrees)")
ax.set_ylabel("Normalized Gain (dB)")
ax.grid(True)
ax.set_ylim(-40, 0)
st.pyplot(fig)

st.markdown("---")
st.markdown("**Note:** This is a simplified visualization. Real-world beamforming involves hardware constraints and propagation channel effects.")
