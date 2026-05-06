# import matplotlib.pyplot as plt # if not using Jupyter notebook, you may need to install matplotlib and uncomment this line
from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.h(0)

state = Statevector.from_instruction(qc)
# print(state)
plot_bloch_multivector(state)
# plt.show()  # if not using Jupyter notebook, you may need to install matplotlib and uncomment this line
