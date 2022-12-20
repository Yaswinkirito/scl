import numpy as np,matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
x=np.sin(t)
plt.stem(t,x)
plt.show()