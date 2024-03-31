import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

x=np.linspace(0,5,10) 
y=pow(x,2)
#fig=plt.figure()

fig=plt.figure(figsize=(8,4),dpi=100)

fig,axes=plt.subplots(figsize=(12,3))
axes.plot(x,y,"r--")
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_title("x-y")
fig.savefig("file1.png") #TO SAVE THE IMAGE
fig.savefig("file2.png",dpi=500) 
fig.savefig("file1.pdf") #pdf exentension supported

plt.show()
