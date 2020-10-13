"""
D-Wave backend implementation.
"""

import os
from dwave.cloud import Client
from ..backend import Backend, Solver
from .solvers import QuboSolver


__all__ = ['DWaveBackend']


class DWaveBackend(Backend):
    def __init__(self, backend_address=os.environ.get('DWAVE_SERVER_ADDRESS'), *args, **kwargs):
        super(DWaveBackend, self).__init__()
        self._backend_address = backend_address
        self._solvers = {
            solver_class.name(): solver_class for solver_class in [QuboSolver]
        }
        self._client = Client(endpoint=backend_address, *args, **kwargs)

    def connect(self):
        """
        Connect to the backend.
        :return: session.
        """
        self._client.session = self._client.create_session()
        return self._client.session

    def disconnect(self):
        """
        Disconnect from the backend.
        :return: None.
        """

        if self._client.session is not None:
            self._client.close()
            self._client.session = None

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

        return self._client.session is not None

    @staticmethod
    def name() -> str:
        """
        Backend name.

        :return: backend name string.
        """

        return 'quantum_dwave'

    @property
    def dwave_client(self) -> Client:
        """
        Return Cloud client.
        :return: Client object.
        """

        return self._client
