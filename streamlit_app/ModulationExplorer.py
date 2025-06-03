import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Modulation Explorer", layout="centered")
st.title("📡 Modulation Explorer")

st.markdown("Explore basic digital modulation schemes: **QPSK**, **16-QAM**, and **64-QAM**.")

# User inputs
mod_scheme = st.selectbox("Choose Modulation Scheme", ["QPSK", "16-QAM", "64-QAM"])
num_symbols = st.slider("Number of Symbols", 50, 2000, 500, step=50)
noise_level = st.slider("Noise Standard Deviation", 0.0, 1.0, 0.2, step=0.05)

def generate_symbols(scheme, N):
    if scheme == "QPSK":
        bits = np.random.randint(0, 2, (N, 2))
        symbols = (2*bits[:, 0] - 1) + 1j*(2*bits[:, 1] - 1)
    elif scheme == "16-QAM":
        bits = np.random.randint(0, 2, (N, 4))
        real = 2*(2*bits[:,0] + bits[:,1]) - 3
        imag = 2*(2*bits[:,2] + bits[:,3]) - 3
        symbols = real + 1j*imag
    elif scheme == "64-QAM":
        bits = np.random.randint(0, 2, (N, 6))
        real = 2*(4*bits[:,0] + 2*bits[:,1] + bits[:,2]) - 7
        imag = 2*(4*bits[:,3] + 2*bits[:,4] + bits[:,5]) - 7
        symbols = real + 1j*imag
    return symbols

# Generate and plot
symbols = generate_symbols(mod_scheme, num_symbols)
noise = noise_level * (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))
received = symbols + noise

fig, ax = plt.subplots()
ax.scatter(received.real, received.imag, alpha=0.6, s=10, color="blue")
ax.set_title(f"{mod_scheme} Constellation with Noise")
ax.set_xlabel("In-Phase")
ax.set_ylabel("Quadrature")
ax.grid(True)
ax.axis("equal")
st.pyplot(fig)
