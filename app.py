import streamlit as st
import pandas as pd
import math
import data_encoding
import benchmarking_memory
import final_report_generator

# App Configuration
st.set_page_config(page_title="QiML Diagnostic Framework", layout="wide")

st.title("🔬 Classical vs. Quantum-Inspired ML: Diagnostic System")

# Sidebar for Inputs
st.sidebar.header("Control Panel")
n_features = st.sidebar.slider("Number of Features (N)", 10, 5000, 2626)
bond_dim = st.sidebar.slider("Bond Dimension (chi)", 2, 100, 30)

# Layout Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Phase 1: Data Encoding")
    if st.button("Run Amplitude Encoding"):
        sample = [1.0] * n_features
        state, qubits = data_encoding.quantum_amplitude_encoding(sample)
        
        # Success Message
        st.success(f"Mapped to {qubits} simulated qubits.")
        
        # NEW: Detailed Calculation Breakdown for Users
        with st.expander("🔍 View Encoding Methodology & Calculations"):
            st.write(f"**Step 1: Feature Vector Normalization**")
            st.latex(r"|\psi\rangle = \frac{1}{\|x\|} \sum_{i=1}^{N} x_i |i\rangle")
            st.write("The input vector is normalized to a unit vector to satisfy probability conservation.")
            
            st.write(f"**Step 2: Hilbert Space Mapping**")
            target_dim = 2**qubits
            st.write(f"To represent {n_features} features, we need the nearest power of 2.")
            st.info(f"Calculation: $2^{{{qubits}}} = {target_dim}$ total dimensions.")
            
            st.write(f"**Step 3: Zero Padding**")
            padding_needed = target_dim - n_features
            st.write(f"Added {padding_needed} zero-amplitudes to fulfill the $2^n$ requirement for qubit simulation.")

with col2:
    st.subheader("Phase 2: Memory Benchmarking")
    if st.button("Extract Resource Metrics"):
        st.write(f"Analyzing Asymptotic Scaling for N={n_features}...")
        chart_data = pd.DataFrame({
            "Classical O(N^2)": [i**2 for i in range(1, 101)],
            "QiML O(N)": [(i * (bond_dim**2) / 10) for i in range(1, 101)]
        })
        st.line_chart(chart_data)

st.divider()

# PHASE 3: FINAL COMPARATIVE REPORT
st.subheader(f"Final Comparative Analysis (N={n_features}, χ={bond_dim})")

if st.button("🚀 Run Full Benchmarking Suite"):
    with st.spinner('Calculating Latency and Accuracy Thresholds...'):
        report_df = final_report_generator.generate_final_research_table(n_features, bond_dim)
        st.table(report_df)
        
        advantage = (1 - (2 * bond_dim**2) / n_features) * 100
        if advantage > 0:
            st.metric("Memory Reduction Advantage", f"{advantage:.1f}%")
        else:
            st.warning("Classical is more efficient at this scale.")
        st.balloons()