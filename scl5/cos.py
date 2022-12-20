import numpy as np,matplotlib.pyplot as plt
t=np.arange(-2*np.pi,2*np.pi,0.1)
a=np.cos(t)
b=np.cos(t)*np.cos(5*t)+np.cos(5*t)
plt.plot(t,a)
plt.show()
plt.plot(t,b)
plt.show()