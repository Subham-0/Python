        # Numpy
'''
numpy stands for numerical python Where we can geta arrays and manupulate those arrays
we have to import a module called numpy then different function can be use.

'''
import numpy as np
arra1 = np.arange(10)
print(arra1)

arr1 = arra1.reshape(2,5)   #for  2d array
print(arr1)

arr2 = arr1.flatten()   #from 2d array to 1d array
print(arr2)

a = np.array([[1,2,3],[2,3,4]])
print(a)

aa = np.ones((2,3),int)
print(aa)

aa = np.zeros((2,3),int)
print(aa)

aa=np.eye(5)
print(aa) 

a = np.reshape(np.arange(11,36,1),(5,5))
print(a)

print(a[0:2,0:3])

print(a[:2,:3])

print(a[2:4,1:4])

print(a[1:4,2:4])

print(a[2:5,3:5])

print(a[2:3,2:3])

b = np.matrix([[4,7,6],[1,2,3]])
print(b)

d = np.diagonal(b)
print(d)

m  = np.max(b)
print(m)
mi  = np.min(b)
print(mi)
mean  = np.mean(b)
print(mean)
m1 = np.sum(b)
print(m1)
mo = np.median(b)
print(mo)

sor = np.sort(b)
print(sor)
