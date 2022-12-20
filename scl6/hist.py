import numpy as np,pandas as pd,matplotlib.pyplot as plt
df=pd.read_csv("gen.csv")
plt.hist(df["sin"])
plt.show()
print(np.mean(df["sin"]),np.std(df["sin"]))
plt.hist(df["cos"])
plt.show()
print(np.mean(df["cos"]),np.std(df["cos"]))