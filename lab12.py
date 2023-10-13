import pandas as pd

s1=pd.Series([3,4,5,6,7,8])
s2=pd.Series([9,8,7,6,5,0])
s3=s1+s2
print(s3)
s3=s1-s2
print(s3)
s3=s1*s2
print(s3)
s3=s1/s2
print(s3)
print("comparison\n")
print(s1>s2)

lst=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
d=pd.DataFrame(lst,columns=['one','two','three'],index=[0,1,2,3])
print(d)

s4=d.iloc[:,0]
print(s4)
s4=d['one'].squeeze()
print(s4)

print("rows=",len(d.index))
print("columns=",len(d.columns))
