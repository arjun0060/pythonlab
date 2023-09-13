string=input("enter a string")
vowel=['a','A','e','E','i','I','o','O','u','U']
it=-1
for i in string:
    it=it+1
    if(i in vowel):
        print(it)
