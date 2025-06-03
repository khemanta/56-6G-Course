import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Scheduler Visualizer", layout="wide")
st.title("📶 Multiple Access & Scheduler Visualizer (Chapter 3)")

st.markdown("""
This tool lets you explore key multiple access techniques in wireless communication:
- FDMA (Frequency Division Multiple Access)
- TDMA (Time Division Multiple Access)
- OFDMA (Orthogonal Frequency Division Multiple Access)
- NOMA (Non-Orthogonal Multiple Access)
- Round Robin & Proportional Fair Scheduling
""")

st.sidebar.header("📊 Settings")
users = st.sidebar.slider("Number of Users", 2, 10, 4)
subcarriers = st.sidebar.slider("Number of Subcarriers (OFDMA)", 4, 32, 16)
slots = st.sidebar.slider("Number of Time Slots", 4, 20, 12)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📡 FDMA & TDMA",
    "🎯 OFDMA",
    "⚡ NOMA",
    "🔁 Round Robin",
    "⚖️ Proportional Fair"
])

with tab1:
    st.subheader("FDMA Allocation")
    fig, ax = plt.subplots(figsize=(8, 2))
    frequencies = np.arange(1, users + 1)
    for i, f in enumerate(frequencies):
        ax.barh(y=i, width=1, left=f, height=0.5, label=f'User {i+1}')
    ax.set_xlabel("Frequency")
    ax.set_yticks(range(users))
    ax.set_yticklabels([f'User {i+1}' for i in range(users)])
    ax.set_title("FDMA: Frequency-Based Resource Allocation")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.subheader("TDMA Allocation")
    fig, ax = plt.subplots(figsize=(8, 2))
    for i, t in enumerate(np.arange(users)):
        ax.bar(x=t, height=1, bottom=i, width=0.8, label=f'User {i+1}')
    ax.set_xlabel("Time Slot")
    ax.set_ylabel("User")
    ax.set_title("TDMA: Time-Based Resource Allocation")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

with tab2:
    st.subheader("OFDMA Subcarrier Allocation")
    allocation = np.random.randint(0, users, subcarriers)
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.bar(range(subcarriers), [1]*subcarriers, color=plt.cm.tab10(allocation))
    ax.set_title("OFDMA Subcarrier Mapping")
    ax.set_xlabel("Subcarrier Index")
    ax.set_yticks([])
    ax.grid(True)
    st.pyplot(fig)

with tab3:
    st.subheader("NOMA Power Domain Multiplexing")
    user1_power = st.slider("Power to User 1 (Far User)", 0.1, 0.9, 0.6)
    user2_power = 1 - user1_power
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.barh([0], user1_power, label="User 1 (Far)")
    ax.barh([0], user2_power, left=user1_power, label="User 2 (Near)")
    ax.set_title("Power Domain in NOMA")
    ax.set_xlabel("Normalized Power")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

with tab4:
    st.subheader("Round Robin Scheduling")
    rr_schedule = [(i % users) + 1 for i in range(slots)]
    fig, ax = plt.subplots(figsize=(10, 1.5))
    ax.bar(range(slots), [1]*slots, color=plt.cm.tab10([u-1 for u in rr_schedule]))
    ax.set_xticks(range(slots))
    ax.set_xticklabels([f'Slot {i+1}' for i in range(slots)], rotation=45)
    ax.set_yticks([])
    ax.set_title("Round Robin Slot Assignment")
    ax.grid(True)
    st.pyplot(fig)

with tab5:
    st.subheader("Proportional Fair Scheduling Example")
    np.random.seed(42)
    inst_rates = np.random.rand(users)
    avg_rates = np.random.rand(users)
    pf_metric = inst_rates / avg_rates

    st.write("User PF Metrics:")
    for i in range(users):
        st.write(f"User {i+1}: Inst Rate = {inst_rates[i]:.2f}, "
                 f"Avg Rate = {avg_rates[i]:.2f}, "
                 f"PF Metric = {pf_metric[i]:.2f}")
    winner = np.argmax(pf_metric)
    st.success(f"🎯 **User {winner+1}** is selected for this slot based on PF scheduling.")
