import matplotlib.pyplot as plt,numpy as np
x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.sinc(x)
plt.plot(x,y)
plt.show()