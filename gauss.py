import numpy as np

def gauss_method(a: np.array, b: np.array, n):
    for i in range(0, n):
        a[i] /= a[i, i]
        b[i] /= a[i, i]
   
        for j in range(0, n):
            if j != i:
                a[j] -= a[i] * a[j, i]
                b[j] -= b[i] * a[j, i]
        for j in range(0, n):
            print(a[j])
        print('  ')
    return b

s = np.array([[1.0, 0.0 , 1.0], [0.0, 1.0, -1.0], [1.0, 1.0, 1.0]], float)
k = np.array([4.0, 3.0, 5.0], float)
l = gauss_method(s, k, 3)
print(l)
