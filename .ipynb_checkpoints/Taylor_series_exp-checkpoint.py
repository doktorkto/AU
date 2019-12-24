import math

inte = 20
def my_ex(x):
    x_pow = x
    mult = 1
    result = 1
    for i in range(1, inte):
        result += x_pow / mult
        x_pow *= x
        mult *= mult + 1
    return result
X = int(input())
print(help(my_ex), my_ex(X))
print(help(math.exp), math.exp(X))
