def prime(num):
    for i in range (2,num):
        if(num%i==0):
            print(num,"is not prime")
            return;
    print(num,"is prime")
inp=int(input("enter a number"))
prime(inp)
            
