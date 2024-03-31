import matplotlib
#import matplotlib.pyplot as plt
import numpy as np
from pylab import *

x=np.linspace(0,5,10) #10 samples points from 0 to 5
#linspace-create that ndarray
print(x)
print(type(x))
y=pow(x,2)
print(y)
#plot(x,y,'r')
#xlabel('timesample')
#ylabel('temperature value')
#title('my  GIFT graph')
#show()

#plot(y,x,'b')
#xlabel('timesample')
#ylabel('temperature value')
#title('my graph')
#show()

subplot(1,3,1) # 1 row 2 columns ist one
plot(x,y,'r--')
subplot(1,3,2)
plot(y,x,'g*-')
subplot(1,3,3)
plot(y,x,'b*-')
show()

x=np.linspace(2,97,100)
y=(-4)*x-10
print(y)
plot(x,y,'m--')
xlabel('x value')
ylabel('y value')
title('negative slope + intercept')
show()

x=np.linspace(5,50,150)
y=3*x+7
subplot(1,2,1)
plot(x,y,'y+')
xlabel('x value')
ylabel('y value')
title('negative slope + intercept')
subplot(1,2,2)
plot(y,x,'b--')
xlabel('x value')
ylabel('y value')
title('negative slope + intercept')
show()

x1=np.linspace(5,50,150)
y1=4*x1-3.5
subplot(2,2,1)
plot(x1,y1,'b:')
xlabel('x value')
ylabel('y value')
subplot(2,2,2)
plot(y1,x1,'y+')
xlabel('x value')
ylabel('y value')
x2=np.linspace(10,150,70)
y2=x2**3+27*x2**2+13*x2+10
subplot(2,2,3)
plot(x2,y2,'k:')
xlabel('x value')
ylabel('y value')
subplot(2,2,4)
plot(y2,x2,'y+')
xlabel('x value')
ylabel('y value')

show()







