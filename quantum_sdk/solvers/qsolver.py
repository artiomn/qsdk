"""
QUBO Solver.
"""
import numpy as np

from backends import Backend, Solver, get_backend_by_name


class QSolver:
    """
    "Quantum" solver.
    """

    def __init__(self, backend: str, *args, **kwargs):
        self._backend: Backend = get_backend_by_name(backend)(*args, **kwargs)
        self._qubo_solver: Solver = self._backend.get_solver('qubo')

    def solve_qubo(self, q: np.array, *args, **kwargs) -> np.array:
        """
        Solve QUBO task.

        :param q: - QUBO matrix.
        :return: result vector.
        """

        return self._qubo_solver.solve(q, *args, **kwargs)
