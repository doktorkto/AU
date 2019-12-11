def bezout(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = bezout(b, a % b)
    return x, y - (a // b) * x, g

t = int(input())
r = int(input())
print(bezout(t, r))
