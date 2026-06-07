import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model_performance(y_true, y_pred, model_name="Model"):
    """
    Implements the Classification Metrics defined in Section D(1) of the paper.
    """
    print(f"\n--- Statistical Validation: {model_name} ---")
    
    # Calculating the 4 core metrics [cite: 148, 149, 150, 151]
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='weighted')
    rec = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    
    print(f"Accuracy:  {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall:    {rec:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    
    return {"acc": acc, "f1": f1}

# --- FACULTY DEMO: Simulated Test Results ---
# Let's simulate a scenario where the QiML model handles noise better [cite: 59]
y_test = [0, 1, 1, 0, 1, 0, 0, 1] # Ground Truth labels

# Classical Model: Struggles with high-dimensional noise 
y_pred_classical = [0, 1, 0, 0, 1, 1, 0, 1] 

# QiML Model: Leveraging Tensor Robustness [cite: 59]
y_pred_qiml = [0, 1, 1, 0, 1, 0, 0, 1] 

# Execute the comparison
evaluate_model_performance(y_test, y_pred_classical, "Classical DNN/SVM")
evaluate_model_performance(y_test, y_pred_qiml, "Quantum-Inspired MPS")