import three_function as l

def inversible(a, n):
    p = l.phi(n)
    if a**p % n == 1:
        return True
    else:
        return False

c = int(input())
m = int(input())
print(inversible(c, m), l.gcd(c, m), l.bezout(c, m))
