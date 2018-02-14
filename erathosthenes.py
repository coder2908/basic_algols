import math
n = int(input())
arr = []
#marking all nos as prime.
for i in range(0,n+1):
    arr.append(True)
arr[1] = False
#marking multiples from 2 to underroot no to false uptill n.
for i in range (2,int(math.sqrt(n))+1):
    if (arr[i] == True):
        for j in range (2*i,n+1,i):
            arr[j] = False
            j = j + i
#printing all values that are true.
for i in range(1,n+1):
    if (arr[i] == True):
        print(i)

        
