import numpy as np,matplotlib.pyplot as plt 
a={"EC":130,"CS":70,"ME":190,"CIVIL":130,"B.Arch":40}
x=list(a.keys())
y=list(a.values())
plt.bar(x,y)
plt.show()