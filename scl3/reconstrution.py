import numpy as np
x=np.array([[1,0,0],[1,1,0],[0,0,1]])
u,s,v=np.linalg.svd(x)
print(f"left singular matrix is \n{u}")
print(f"Diagonal matrix is \n{s}")
print(f"right singular matrix is \n{v}")
print(np.round(u@np.diag(s)@v))