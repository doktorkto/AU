import sys
import numpy as np 

#a - matrix nxn of coefficients, b - rigth side in every par in this system, n - size of leg this matrix
def gauss_method(a: np.array, b: np.array, n):  
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            a[i, j] /= a[i, i]
        b[i] = b[i] / a[i, i]
        for j in range(i + 1,n - 1):
            for k in range(i, n - 1):
                a[j, k] -= a[i, k] * a[j, i]
            b[j] -= b[i] * a[j, i]
    for i in range(0, n - 1):
        for j in range(0, n - 2 - i):
            a[n - 2 - i - j, n - 1 - i] -= a[n - 1 - i, n - 1 - i] * a[n - 2 - i - j, n - 1 - i]
            b[n - 2 - i - j] -= b[n - 1 - i] * a[n - 1 - i, n - 1 - i]
    return b

s = np.array([[0.0, 2.0, 1.0], [1.0, 0.0 , 1.0], [0.0, 1.0, 1.0]], float)
k = np.array([4.0, 2.0, 1.0], float)
l = np.zeros(3)
l = gauss_method(s, k, 3)
for i in range(0, 2):
    print(l[i])
