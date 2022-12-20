import numpy as np
a=np.array([[0,1,2],[3,4,5],[6,7,8]])
b=np.array([[-4,-3,2],[0,2,1],[1,4,2]])
print(a+b)#first question
print(np.add(a,b))
y=b.copy()#second question
y[0]=np.add(y[0],2)
print(y)
x=a.copy()#third question
print(np.sum(x))
z=b.copy()#fourth question
z=z.transpose()
s=np.array([0,0,0])
for i in range(3):
    s[i]=np.sum(z[i][:])
print(s)
print(np.multiply(a,b))#fifth question

