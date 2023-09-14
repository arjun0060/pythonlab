studname=[]
n=int(input("enetr the number of students"))
for i in range (n):
    name=input("enter the name of student ")
    studname.append(name)
print(studname)
print("name with starting lettters from a through m :")
for i in range (n):
    firstletter=studname[i].lower()
    if firstletter[0] in ("abcdefghijklm"):
        print(firstletter)
