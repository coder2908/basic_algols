# uses python 3

a = int(input("Enter num 1 : ").strip())
b = int(input("Enter num 2 : ").strip())

if (a < b):
    a, b = b, a

def gcd_extended(a,b):
    if b == 0:
        return a, 1, 0
    else:
        d, p, q = gcd_extended(b, a % b)
        x = q
        y = p - q * (a // b)
        return d, x, y

d, x, y = gcd_extended(a,b)

print(f"The gcd of {a} and {b} is {d} which is equal to {a}*{x} + {b}*{y} = {d}")
