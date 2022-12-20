import numpy as np,matplotlib.pyplot as plt
t=np.arange(0,100,0.01)
T=20
n=int(input("N: "))
sum=0
for i in range(0,n-1):
    f=(-1)**(i)*(np.cos((2*np.pi*(2*i+1)*t)/T))/(2*i+1)
    sum=sum+4*f/np.pi
plt.plot(t,sum)
plt.show()