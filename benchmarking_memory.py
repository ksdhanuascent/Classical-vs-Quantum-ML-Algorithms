import numpy as np
import sys
import time

def benchmark_scaling(n_features, bond_dim=10):
    print(f"\n--- Comparative Analysis for N = {n_features} ---")
    
    # 1. CLASSICAL ARCHITECTURE SCALING (DNN/SVM)
    # A standard weight matrix scales quadratically O(N^2)
    start_class = time.time()
    classical_weights = np.random.rand(n_features, n_features)
    classical_mem = sys.getsizeof(classical_weights) / (1024**2) # Convert to MB
    latency_class = time.time() - start_class
    
    # 2. QI-ML ARCHITECTURE SCALING (MPS)
    # MPS decomposes this into a chain of smaller tensors
    start_qi = time.time()
    # Simulating N tensors of shape (bond, physical, bond)
    mps_tensors = [np.random.rand(bond_dim, 2, bond_dim) for _ in range(n_features)]
    qi_mem = sum(sys.getsizeof(t) for t in mps_tensors) / (1024**2) # Convert to MB
    latency_qi = time.time() - start_qi
    
    # Output Results
    print(f"Classical Memory Usage: {classical_mem:.4f} MB")
    print(f"Quantum-Inspired Memory: {qi_mem:.4f} MB")
    
    if qi_mem < classical_mem:
        reduction = ((classical_mem - qi_mem) / classical_mem) * 100
        print(f"RESULT: QiML achieved {reduction:.2f}% memory reduction.")
    else:
        print("RESULT: Classical is still more efficient at this scale.")

# Run for two different scales to show the 'Crossover Point'
benchmark_scaling(100)   # Small scale
benchmark_scaling(2000)  # High-dimensional scale
