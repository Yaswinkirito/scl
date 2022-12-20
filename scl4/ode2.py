import numpy as np
from scipy.integrate import odeint
def model(u,t):
    return (u[1],-2*u[1]-2*u[0]+np.exp(-t))
u0=[0,0]
t=np.linspace(0,10,10)
op=odeint(model,u0,t)
print(op[:,0])