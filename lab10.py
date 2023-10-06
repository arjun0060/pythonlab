import numpy as np
a=np.arange(10)
b=np.arange(20,10,-1)
print(a)
print(b)
c=np.hstack((a,b))
print(c)
n=int(input("enter the element to be searched"))
temp=0
for i in c:
    if(i==n):
        temp=1
if(temp==1):
    print("element found")
else:
    print("element not found")
d=np.sort(c)
print("sorted array is",d)
for i in range (0,6):
    c[i]=10
print(c)
