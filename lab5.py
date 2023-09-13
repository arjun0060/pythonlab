lst=[]
n=int(input("enter the number of elements"))
for i in range (n):
    el=input("enter the element")
    lst.append(el)
for i in lst:
    print(i[0:3])
