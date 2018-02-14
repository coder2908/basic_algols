#uses python 3
import math
def isprime(n):
    sqrt=int(math.sqrt(n))
    for i in range(2,sqrt+1):
        if(n % i == 0):
            return 0
            break
    return 1

n = int(input("Enter total no of nos : ").strip())
nos = []
prime = []
for i in range(0, n):
    nos.append(int(input(f"Enter no {i} :").strip()))
nos.sort()

for i in range(2,nos[n-1]+1):
    if(isprime(i) == 1):
        prime.append(i)

c1 = 0
res = 1
for i in prime:
    for j in range(0, len(nos)):
        if (nos[j] != 1):
            if (nos[j] % i == 0):
                nos[j] = nos[j] / 2
                c1+= 1
            else:
                continue
            if (c1 > 0):
                res = res * i
    c1 = 0
print(res)

