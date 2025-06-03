 **README File >**

# 📘 Chapter 1 — Introduction to Wireless Communication

## ✅ The CellCoverage.py Streamlit app page has been successfully generated!

### This app includes:

- 📡 Frequency selector (0.7 GHz – 6 GHz)
- 📏 Max Distance slider (10 – 5000 meters)
- 🏙️ Path Loss Exponent control (1.0 – 6.0)

### It visualizes:

- Free Space Path Loss (FSPL)
- Log-distance Path Loss
- 👉 Download CellCoverage.py



## ✅ 1. Deploy the Streamlit App (Locally or on EC2/Cloud)

### Option A: Local Deployment

#### If you want to test it locally:

```bash
# Step 1: Install Streamlit if not already
pip install streamlit

# Step 2: Run the app
streamlit run CellCoverage.py
```

### Option B: Deploy on EC2/Remote Server

> SSH into your server

```bash
ssh -i your_key.pem username@your-ec2-ip
```

> Install Streamlit and dependencies

```bash
pip install streamlit matplotlib numpy
```

> Copy file using scp

```bash
scp -i your_key.pem CellCoverage.py username@your-ec2-ip:/home/ubuntu/
```

> Run the app on a specific port

```bash
streamlit run CellCoverage.py --server.port 8501 --server.address 0.0.0.0
```

> Open in browser

Visit: http://<your-ec2-ip>:8501

If you want help with EC2 setup, security group config, or reverse proxy (Nginx + HTTPS).


## ✅ 2. LaTeX Appendix Section for A1: Signal Strength
Here’s the appendix content (appendix-A1.tex) that will be included in your full LaTeX book:


## ✅ 3. Start Chapter 2 and A2 Notebook


# 📘 Chapter 2: Spectrum & Modulation in 5G

📘 Chapter 2: Spectrum & Modulation
📓 A2-ofdm_simulation.ipynb notebook with visuals
🧪 ModulationExplorer.py Streamlit app (optional)

We’ll cover:

- What is Spectrum?
- Licensed vs Unlicensed Bands
- Frequency Allocation for 5G
- OFDM and Modulation Techniques (QAM, PSK, etc.)
- Appendix A2: OFDM Signal Simulation

Generate the A2-ofdm_simulation.ipynb, and 
Streamlit app for simulation ?

👉 Let me know if you want visuals for OFDM signals (time & frequency domain).
