import numpy as np
from numba import njit, prange

s = np.array([[2.0, 1.0 , 1.0], [4.0, 1.0, 1.0], [2.0, 1.0, -1.0]], float)
k = np.array([2.0, 6.0, 4.0], float)

@njit(fastmath=True)
def gauss_method(a: np.array, b: np.array, n):
    for i in range(0, n):
        b[i] /= a[i, i]
        a[i] /= a[i, i]
   
        for j in range(0, n):
            if j != i:
                b[j] -= b[i] * a[j, i]
                a[j] -= a[i] * a[j, i]
    return b

gauss_method(s, k, 3)
%timeit gauss_method(s, k, 3)
