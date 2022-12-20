import numpy as np
x=np.array([[1,0,0],[1,1,0],[0,0,1]])
u,s,v=np.linalg.svd(x)
i=int(input("No of terms required: "))
print(np.round(u[:,:i]@np.diag(s[:i])@v[:i,:]))