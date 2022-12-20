import matplotlib.pyplot as plt,numpy as np
def main():
    t=np.arange(0,2*np.pi,0.01)
    plot(t,np.sin(t),["t","sin(t)","sin"])
    plot(t,np.cos(t),["t","cos(t)","cos"])
    plot(t,np.sinh(t),["t","sinh(t)","sinh"])
    plot(t,np.cosh(t),["t","cosh(t)","cosh"])
def plot(x,y,z):
    plt.xlabel(z[0])
    plt.ylabel(z[1])
    plt.title(z[2])
    plt.plot(x,y)
    plt.show()
if __name__=="__main__":
    main()