"""
Ising basis class and routines.
"""


class IsingBasis:
    """
    Ising basis class.
    """

    def __init__(self, h, j):
        self._h = h
        self._j = j

    @property
    def h(self):
        return self._h

    @property
    def j(self):
        return self._j
