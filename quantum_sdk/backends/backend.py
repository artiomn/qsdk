"""
Backend base class and generic routines.
"""

from abc import ABC, abstractmethod
from typing import Iterable


class Solver(ABC):
    """
    Solver base class.
    """

    @abstractmethod
    def solve(self, *args, **kwargs) -> Iterable[int]:
        """
        Solve task.

        :param args: task positional parameters.
        :param kwargs: task named parameters.
        :return: result vector.
        """

        raise NotImplemented()

    @staticmethod
    @abstractmethod
    def name() -> str:
        """
        Solver name.

        :return: solver name string.
        """

        raise NotImplemented()


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
    def get_solver(self, name: str) -> Solver:
        """
        Return solver by name.

        :param name: solver name.
        :return: solver object.
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

    @staticmethod
    @abstractmethod
    def name() -> str:
        """
        Backend name.

        :return: backend name string.
        """

        raise NotImplemented()
