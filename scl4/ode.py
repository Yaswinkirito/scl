from scipy.integrate import odeint
import numpy as np
def model(y,t):
    k=-2
    dydt=k*y
    return dydt
y0=1
t=np.linspace(0,10,10)
print(odeint(model,y0,t))