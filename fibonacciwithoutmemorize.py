import timeit
def f(x):
    value = 0
    if x < 1:
        return 0
    if x == 1 or x == 2:
        return 1;
    else:
        return f(x - 1) + f(x - 2)
    
d = int(input())
print(f(d))
timeit.timeit(number = 1000)
