# How to call a static method?
class A:
    def a(self): #static method
        print(1)
class B:
    def a(self):
        print(2)
class C:
    def a(self):
        print(3)
        
class D(A,B,C):
    def x1(self):
        A.a(self)
        B.a(self)
        C.a(self)
ob = D()
ob.x1()
# C.a(self)
print("__________________________________\n")
from abc import ABC
class AB(ABC):
    def x1(self):
        pass
    def x2(self):
        print(2)
class ABB(AB):
    def x1(self):
        print(1)
    def x3(self):
        print(3)
ob = ABB()
ob.x1()
ob.x2()
ob.x3()
print("___________")
ob1 = AB()
ob1.x2()
ob1.x1()

# InterFace in python
#  ->In interface all the methods are abstract.
#  it does not contain any non abstract methods.
#  We are not writting any key word called interface 
#  All will be written inside the class because all the methods are abstarct so it is interface

# Advantage of abstract class and Interface