#!/bin/bash
git clone https://github.com/subhash-nmimsshirpur/intro-to-quantum-computing.git
cd intro-to-quantum-computing/ 
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip -V
python -V
pip install -r requirements.txt
python test_qiskit.py