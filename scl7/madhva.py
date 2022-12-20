import numpy as np
n=int(input("N: "))
sum=0
for i in range(0,n-1):
    f=((-1)**(i))/(2*i+1)
    sum=sum+4*f
print(sum)
