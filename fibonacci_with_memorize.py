import functools
import timeit

@functools.lru_cache()
def fib_2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_2(n-1) + fib_2(n-2)
k = int(input())
for n in range(1, k + 1):
    print(n, fib_2(n))
timeit.timeit(number = 1000)
