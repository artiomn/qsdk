"""
Local optimizer backend implementation.
"""

# Some arbitrary local optimizer.
from optimizer import Optimizer

from ..backend import Backend, Solver
from .solvers import QuboSolver


__all__ = ['LocalBackend']


class LocalBackend(Backend):
    def __init__(self, *args, **kwargs):
        super(LocalBackend, self).__init__()
        self._solvers = {
            solver_class.name(): solver_class for solver_class in [QuboSolver]
        }

        self._optimizer = Optimizer(*args, **kwargs)

    def connect(self):
        """
        Connect to the backend. Stub.
        :return: session.
        """
        pass

    def disconnect(self):
        """
        Disconnect from the backend. Stub.
        :return: None.
        """
        pass

    def get_solver(self, name: str) -> Solver:
        """
        Return solver by name.

        :param name: solver name.
        :return: solver object.
        """

        return self._solvers[name](self)

    @property
    def connected(self) -> bool:
        """
        Return backend connection state.

        :return: connection state.
        """

        return True

    @staticmethod
    def name() -> str:
        """
        Backend name.

        :return: backend name string.
        """

        return 'local_optimizer'
