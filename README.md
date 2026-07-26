Classical vs Quantum Machine Learning Algorithms

A comparative study and benchmark analysis exploring the implementation, performance, execution time, and accuracy of **Classical Machine Learning (CML)** versus **Quantum Machine Learning (QML)** algorithms.

---

## 📌 Project Overview

Quantum Machine Learning (QML) leverages principles of quantum mechanics—such as superposition, entanglement, and interference—to process complex, high-dimensional datasets. This repository provides an empirical comparison between classical algorithms (like SVM, Random Forest, Logistic Regression) and their quantum counterparts (such as Quantum Support Vector Classifier, Variational Quantum Classifier, Quantum Neural Networks) across standard benchmarks.

### Key Focus Areas:
- **Performance Evaluation**: Comparison of precision, recall, F1-score, and accuracy across dataset types.
- **Execution Speed & Scalability**: Analyzing quantum circuit overhead and runtimes as data dimensionality and instance counts scale.
- **Quantum Feature Encodings**: Demonstrating Basis Encoding, Angle Encoding, and Amplitude Encoding techniques.

---

## 🛠️ Tech Stack & Frameworks

- **Language**: Python 3.8+
- **Quantum Computing Frameworks**: 
  - [Qiskit](https://qiskit.org/) / Qiskit Machine Learning
  - [PennyLane](https://pennylane.ai/)
- **Classical Machine Learning & Utilities**:
  - `scikit-learn`
  - `numpy`, `pandas`
  - `matplotlib`, `seaborn` (Data Visualization)
 
  🚀 Getting Started
Prerequisites
Ensure you have Python 3.8 or higher installed on your system.

Installation
Clone the repository:

Bash
git clone [https://github.com/ksdhanuascent/Classical-vs-Quantum-ML-Algorithms.git](https://github.com/ksdhanuascent/Classical-vs-Quantum-ML-Algorithms.git)
cd Classical-vs-Quantum-ML-Algorithms
Create and activate a virtual environment (recommended):

Bash
# On macOS/Linux
python3 -m venv qml_env
source qml_env/bin/activate

# On Windows
python -m venv qml_env
qml_env\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
💻 Usage
Run the main comparative experiment script:

Bash
python main.py
Or explore the step-by-step implementations in the Jupyter Notebooks:

Bash
jupyter notebook
