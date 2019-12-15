import random
import sys
from math import gcd

def rabin_miller(x: int):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    
    s, f = 0, x - 1
    while f % 2 == 0:
        s+= 1
        f //= 2
    to_test = (random.randint(2, x - 1) for _ in range(50))
    for a in to_test:
        cur = pow(a, f, x)
        if cur == 1:
            return False
        if cur == x - 1:
            break
        else:
            return False
    return True
f = int(input())
print(rabin_miller(f))
