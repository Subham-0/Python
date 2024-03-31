import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

n=np.array([0,1,2,3,4,5])
x=np.linspace(0,5,10)
xx=np.linspace(-0.75,1.,100)
print(x)
print(len(xx))

fig,axis=plt.subplots(1,4,figsize=(12,3))
axis[0].scatter(xx,xx+0.75*np.random.randn(len(xx)))
axis[0].set_title("scatter")

axis[1].step(n,n**2,lw=2)
axis[1].set_title("step")

axis[2].bar(n,n**2,align="center",width=0.5,alpha=0.5)
axis[2].set_title("bar")

axis[3].fill(n,n**2)
plt.show()
