# intro-to-quantum-computing
My repo to test quantum computing frameworks Qiskit and Cirq

## Qiskit Installation

### On Linux systems -
```
git clone https://github.com/subhash-nmimsshirpur/intro-to-quantum-computing.git
cd intro-to-quantum-computing/ 
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip -V
python -V
pip install -r requirements.txt
python test_qiskit.py
```

### On Windows systems -
```
open cmd
mkdir intro-to-quantum-computing
cd intro-to-quantum-computing
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip -V
python -V
pip install qiskit cirq matplotlib
python test_qiskit.py
```

### Installing and using Jupyter Notebook from this folder
```
pip install notebook
jupyter notebook
``` 

