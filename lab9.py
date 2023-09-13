
choice=1
while(choice!=5):
    print("enter your choice\n1.add\n2.subtract\n3.multiply\n4.divide\n")
    choice=int(input())
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    if(choice==1):
        print( a+b)
        break
    elif(choice==2):
        print(a-b)
        break
    elif(choice==3):
        print (a*b)
        break
    elif(choice==4):
        print (a/b)
        break
    else:
        print("invalid choice")
