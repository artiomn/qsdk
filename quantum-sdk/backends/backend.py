"""
Backend base class and generic routines.
"""

from abc import ABC, abstractmethod
from typing import Iterable


class Backend(ABC):
    """
    All backends base.
    """

    @abstractmethod
    def connect(self):
        """
        Connect to the backend.
        :return: None.
        """
        raise NotImplemented()

    @abstractmethod
    def disconnect(self):
        """
        Disconnect from the backend.
        :return: None.
        """
        raise NotImplemented()

    @abstractmethod
    def solve_qubo(self, q_matrix) -> Iterable[int]:
        """
        Solve QUBO problem.

        :param q_matrix: QUBO Q matrix as a numpy array.
        :return: result vector.
        """

        raise NotImplemented()

    @property
    @abstractmethod
    def connected(self) -> bool:
        """
        Return backend connection state.

        :return: connection state.
        """

        raise NotImplemented()
