import numpy as np
from graph import plot#graph.py program plot function
t=np.arange(-5,5,0.01)
f=4*(t**2)+3
plot(t,f,["t","f(t)","f(t)"])

