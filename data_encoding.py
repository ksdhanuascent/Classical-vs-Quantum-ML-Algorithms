import numpy as np

def quantum_amplitude_encoding(feature_vector):
    """
    Transforms classical features into a simulated quantum state vector.
    Follows Equation in Section II-A(2) of the methodology.
    """
    # 1. Classical Standardization (Mean=0, Std=1) 
    x = np.array(feature_vector)
    x_standardized = (x - np.mean(x)) / (np.std(x) + 1e-8) # Added epsilon to prevent div by zero
    
    # 2. Determine required dimension (2^n) 
    n_features = len(x_standardized)
    num_qubits = int(np.ceil(np.log2(n_features)))
    target_dim = 2**num_qubits
    
    # 3. Padding with zeros to reach 2^n 
    padded_vector = np.zeros(target_dim)
    padded_vector[:n_features] = x_standardized
    
    # 4. Amplitude Normalization 
    # Magnitude ||x|| must be 1 so that sum(|x_i|^2) = 1
    norm = np.linalg.norm(padded_vector)
    if norm == 0:
        quantum_state = padded_vector
    else:
        quantum_state = padded_vector / norm
        
    return quantum_state, num_qubits


# Sample data: 10 features (e.g., from a sensor or medical record)
sample_features = [23.5, 1.2, -5.6, 8.9, 0.4, 12.1, 7.7, -2.3, 4.5, 6.1]

state_vector, q_count = quantum_amplitude_encoding(sample_features)

print("--- Quantum Amplitude Encoding Report ---")
print(f"Original Features: {len(sample_features)}")
# REMOVED THE  FROM HERE TO FIX THE ERROR
print(f"Simulated Qubits Required: {q_count}") 
print(f"State Vector Dimension: {len(state_vector)}")
print(f"Normalization Check (Sum of Squares): {np.sum(state_vector**2):.4f}")
print("\nEncoded State Vector (First 5 components):")
print(state_vector[:5])