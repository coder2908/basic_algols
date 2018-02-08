#using python 3
#using euclig algol to find gcd
big = int(input())
small = int(input())
if (big < small):
    small,big = big,small
temp = 1
while(temp != 0):
    temp = big % small
    big, small = small,temp
print(f"the gcd is  : {big}") 
