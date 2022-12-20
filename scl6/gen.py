import pandas as pd,numpy as np,matplotlib.pyplot as plt
t=np.arange(0,2*np.pi,0.1)
a=np.sin(t)
b=np.cos(t)
df=pd.DataFrame({"time":t,"sin":a,"cos":b})
df.to_csv("gen.csv")