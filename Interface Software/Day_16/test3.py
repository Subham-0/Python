from turtle import color
import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([1,2,6,8])
ypoint = np.array([3,8,1,10])

# xpoint = np.array([0,1,2,3])
# ypoint = np.array([3,8,1,10])

#Test single single line 
# plt.plot(xpoint,ypoint,'x')
# plt.plot(ypoint,'o:r')
# plt.plot(ypoint,marker = 'o',ms = '10',mec = 'g')
# plt.subplot(1,2,1)
# plt.scatter(xpoint,ypoint)
# plt.bar(xpoint,ypoint)
# plt.barh(xpoint,ypoint)
# plt.bar(xpoint,ypoint,color='r',width=0.1)
plt.barh(xpoint,ypoint,color='r',height=0.5)



plt.show()