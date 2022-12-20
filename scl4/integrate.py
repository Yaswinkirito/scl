from scipy.integrate import quad
i,err= quad(lambda x:4*(x**2)+3,-2,2)
print(i)