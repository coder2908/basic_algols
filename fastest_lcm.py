#uses python 3
#to find lcm between set of integers.
#----------------------------------------#
n = int(input("enter no of nos to be entered").strip())
#getting total nos of integers.
nos = []
for i in range(0,n,1):
    nos.append(int(input("enter no.").strip()))
nos.sort()
res = 1
for i in range(0,len(nos)):
    counter = 0
    temp = nos[i]
    for j in range(i,len(nos)):
        if (temp!=1):
            if(nos[j] % temp == 0):
                counter = counter + 1
                nos[j] = nos[j] / temp
    if (counter >= 1):
        res = res * temp
    nos.sort()
print(res)
