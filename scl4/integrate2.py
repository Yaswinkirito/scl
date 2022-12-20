from scipy.integrate import quad
import numpy as np
i,err=quad(lambda x:np.exp(-x)*np.sin(3*x),0,2*np.pi)
print(i)