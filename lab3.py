dict1={}
n=int(input("enter the number of elements"))
for i in range (n):
    key=input("enter the key ")
    value=int(input("enter the value "))
    dict1[key]=value
print("printing even values")
for key,value in dict1.items():
    if(value%2==0):
        print(f"{key}:{value}")
