from turtle import color
import matplotlib.pyplot as plt
import numpy as np


y = np.array([23,45,34,2])
mylabels = ["apple","banana","cherry","graphs"]
myexplode = [0.05,0.05,0.05,0.05]
# plt.xlabel("text1")
# plt.ylabel("text2")
plt.title("TEST FOR MATHPLOTLIB")



plt.pie(y,labels=mylabels,startangle=90,explode=myexplode)
plt.legend(loc='right')
#'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
plt.show()
