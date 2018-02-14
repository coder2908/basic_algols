#Uses python 3
l = int(input())
str = input()
str = str.split()
n = []
for i in range(0,len(str)):
    n.append(int(str[i]))
assert(l == len(n))
n.sort()
l = len(n)
a , b = n[l-1], 0
for i in range(l-1,0,-1):
    if (n[i] != a):
        b = n[i]
        break
print(a*b)

