import numpy as np
a=np.arange(10)
print(a)
b=np.append(a,12)
print(b)
print("reverse=",np.flip(b))
c=np.asfarray(b)
print(c)
maximum=np.argmax(b)
minimum=np.argmin(b)
print("index of maximum value=",maximum)
print("index of minimum value=",minimum)
