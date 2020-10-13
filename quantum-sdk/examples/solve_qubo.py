import numpy as np
from quantum_sdk import QSolver

qsolver = QSolver(backend='quantum')
Q = np.random.rand(5, 5)
s = qsolver.solve_qubo(Q)

# result: s = [1,0,0,1,1]
