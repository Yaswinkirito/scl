import pandas as pd,matplotlib.pyplot as plt
df=pd.read_csv("gen.csv")
plt.plot(df["time"],df["sin"],color="orange")
plt.plot(df["time"],df["cos"],color="blue")
plt.show()