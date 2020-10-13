"""
QUBO basis class and routines.
"""


class QUBOBasis:
    """
    QUBO basis class.
    """

    def __init__(self, q_matrix):
        self._q = q_matrix

    @property
    def q(self):
        return self._q
