import numpy as np
x=np.array([[1,3,3],[1,4,5],[1,3,4]])
if np.linalg.det(x)!=0:
    print(np.linalg.inv(x))
else:
    print("Inverse doesn't exist")
