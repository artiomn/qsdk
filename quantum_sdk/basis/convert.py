from typing import Tuple

import numpy as np


def from_ising_to_qubo(h: np.array, j: np.array) -> np.array:
    """
    Ising to QUBO converter.
    Solution from the `dimod.utilities.ising_to_qubo`, but for the Numpy arrays.

    :param h: from value in the Ising basis.
    :param j: from value in the Ising basis.
    :return: value in the QUBO basis.
    """

    q = np.diag([h[i, i] * 2. for i in range(len(h))])

    # next the quadratic biases
    for u, row in enumerate(j, start=1):
        for v, bias in enumerate(row, start=1):
            if bias == 0.0:
                continue
            q[u, v] = 4. * bias
            q[u, u] -= 2. * bias
            q[v, v] -= 2. * bias

    return q


def from_qubo_to_ising(q: np.array) -> Tuple[np.array, np.array]:
    """
    QUBO to Ising converter.
    Solution from the `dimod.utilities.qubo_to_ising`, but for the Numpy arrays.

    :param q: from value in the QUBO basis.
    :return: value in the Ising basis (h, J).
    """

    h = {}
    j = {}
    linear_offset = 0.0
    quadratic_offset = 0.0

    for u, row in enumerate(q, start=1):
        for v, bias in enumerate(row, start=1):
            if u == v:
                if u in h:
                    h[u] += .5 * bias
                else:
                    h[u] = .5 * bias
                linear_offset += bias

            else:
                if bias != 0.0:
                    j[u, v] = .25 * bias

                if u in h:
                    h[u] += .25 * bias
                else:
                    h[u] = .25 * bias

                if v in h:
                    h[v] += .25 * bias
                else:
                    h[v] = .25 * bias

                quadratic_offset += bias

    return h, j
