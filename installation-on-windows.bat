mkdir intro-to-quantum-computing
cd intro-to-quantum-computing
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip -V
python -V
pip install qiskit cirq matplotlib
python test_qiskit.py