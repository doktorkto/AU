def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def bezout(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = bezout(b, a % b)
    return (x, y - (a // b) * x, g)

def phi(n):
    result = n
    for i in range(2, n):
        if n % i == 0:
            while n % i ==0:
                n /= i
            result -= result / i
    if n > 1:
        result -= result / n
    return result
