#prime printer using square root algorithms.
import math
t = int(input())
al = []
line = []
l = 0
u = 0
def isprime(n):
    sqrt=int(math.sqrt(n))
    for i in range(2,sqrt+1):
        if(n % i == 0):
            return 0
            break
    return 1
for i in range(0,t):
    if (t<=10):
        al.append(input())
for j in range(0,t):
    line = al[j].split(" ")
    l = int(line[0])
    if (l == 1):
        l = 2
    u = int(line[1])
    for i in range(l,u+1):
        if(isprime(i) == 1):
            print(i)
    print("\n")
