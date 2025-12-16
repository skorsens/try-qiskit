from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


"""
Implement and visualize the Hadamard gate circuit (See https://en.wikipedia.org/wiki/Hadamard_transform).

Hadamard gate puts a qubit in an equal superposition of 0 and 1.

Running the circuit and measuring the value of its qubit requires execution on a simulator
"""

def CreateHadamardQuantumCircuit(bVisualize: bool = True) -> QuantumCircuit:
    """Create the Hadamard gate circuit."""

    # Create a quantum register to hold a qubit
    qr = QuantumRegister(1, name="quantum_register")
    # Create a classical register to hold the results of the qubit measurement
    cr = ClassicalRegister(1, name="classical_register")
    # Create a quantum circuit that combines the registers
    qc = QuantumCircuit(qr, cr)

    # Visualize the circuit without any gates applied
    qc.draw("mpl", filename="quantum_circuit_no_gates.png")

    # Apply the Hadamard gate to the first quantum resgisters of the circuit
    qc.h(0)
    # Visualize the circution with the gate applied
    qc.draw("mpl", filename="quantum_circuit_hadamard_gate.png")

    # Measure the qubit
    qc.measure(0, 0)
    qc.draw("mpl", filename="quantum_circuit_measure.png")

    return qc


if __name__ == "__main__":
    CreateHadamardQuantumCircuit(False)
