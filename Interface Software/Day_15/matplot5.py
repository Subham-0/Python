import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
x=np.linspace(0,5,10) 
y=pow(x,2)
fig=plt.figure()
fig,ax=plt.subplots()
ax.plot(x,x**2,label="Blue")
ax.plot(x,x**3,label="Red")
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("x-y")

plt.show()
