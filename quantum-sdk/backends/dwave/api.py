"""
D-Wave backend implementation.
"""
from typing import Iterable

from ..backend import Backend


__all__ = ['DWaveBackend']


class DWaveBackend(Backend):
    def __init__(self, backend_address):
        super(DWaveBackend, self).__init__()

    def connect(self):
        """
        Connect to the backend.
        :return: None.
        """
        raise NotImplemented()

    def disconnect(self):
        """
        Disconnect from the backend.
        :return: None.
        """
        raise NotImplemented()

    def solve_qubo(self, q_matrix) -> Iterable[int]:
        """
        Solve QUBO problem.

        :param q_matrix: QUBO Q matrix as a numpy array.
        :return: result vector.
        """

        raise NotImplemented()

    @property
    def connected(self) -> bool:
        """
        Return backend connection state.

        :return: connection state.
        """

        raise NotImplemented()
