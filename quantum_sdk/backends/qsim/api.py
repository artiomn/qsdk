"""
Local optimizer backend implementation.
"""

# Russian Quantum Center
import RQCSimClient

from ..backend import Backend, Solver
from .solvers import QuboSolver


__all__ = ['QuantumSimulationBackend']


class QuantumSimulationBackend(Backend):
    def __init__(self, backend_address, *args, **kwargs):
        super(QuantumSimulationBackend, self).__init__()
        self._backend_address = backend_address
        self._solvers = {
            solver_class.name(): solver_class for solver_class in [QuboSolver]
        }
        self._client = RQCSimClient(endpoint=backend_address, *args, **kwargs)

    def connect(self):
        """
        Connect to the backend.
        :return: None.
        """
        self._client.connect()

    def disconnect(self):
        """
        Disconnect from the backend.
        :return: None.
        """

        self._client.disconnect()

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

        return self._client.is_connected()

    @staticmethod
    def name() -> str:
        """
        Backend name.

        :return: backend name string.
        """

        return 'rqc_simulator'
