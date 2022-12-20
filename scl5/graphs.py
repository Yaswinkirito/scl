import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(170, 50,25)
plt.stem(x)
plt.show()
plt.plot(x)
plt.show()
plt.boxplot(x)
plt.show()
y = np.random.normal(170,50, 25)
plt.scatter(x,y)
plt.show()
data = { 'EC':  np.random.randint(0,200),
 'CS':  np.random.randint(0,200), 'ME':np.random.randint(0,200), 'CIVIL' :np.random.randint(0,200), 'B.Arch' :np.random.randint(0,200)}
courses = list(data.keys())
values = list(data.values())
plt.bar(courses, values, color ='blue',
        width = 0.4)
plt.show()
