import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)
qc.h(0)
qc.z(0)
qc.draw('mpl')

plt.show()