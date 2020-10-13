"""
D-Wave solvers.
"""

from typing import Iterable

from ..backend import Solver


__all__ = ['QuboSolver']


class QuboSolver(Solver):
    def __init__(self, backend):
        """
        :param backend: backend object.
        """
        super(QuboSolver, self).__init__()

        self._backend = backend
        self._solver = backend.get_solver('qubo')

    def solve(self, q_matrix, *args, **kwargs) -> Iterable[int]:
        """

        :param q_matrix: Q - QUBO parameters matrix.
        :param args: arguments will be passed the real solver.
        :param kwargs: arguments will be passed the real solver, i.e. `num_reads=100`.
        :return: solver result vector.
        """
        return self._solver.sample_qubo(q_matrix, *args, **kwargs)

    @staticmethod
    def name() -> str:
        return 'qubo'
