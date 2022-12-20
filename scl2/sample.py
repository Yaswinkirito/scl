import matplotlib.pyplot as plt,numpy as np
fs=10000
f=10
T=np.arange(fs/f)/fs
x=np.sin(2*np.pi*f*T)
plt.plot(T,x)
plt.show()