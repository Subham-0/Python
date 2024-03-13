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
from ast import Try
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
print("_______________")

# InterFace in python
#  ->In interface all the methods are abstract.
#  it does not contain any non abstract methods.
#  We are not writting any key word called interface 
#  All will be written inside the class because all the methods are abstarct so it is interface

# Advantage of abstract class and Interface
'''
    When in a child class method name are same and deffinations are different then we can keep that method as abstract in the super class/base class.
    By using abstract class we can make the object light
    

'''
from abc import ABC
class AC:
    def x1(self):
        pass
    def x2(self):
        print(2)
        
class AC1(AC):
    def x1(self):
        print(1)
    def x3(self):
        print(3)
        
ob = AC1()
ob.x1()
ob.x2()
ob.x3()
ob1 = AC()
ob1.x2()
print("___________________")

#Interface
'''
When a class contain all abstract methods then it is called as interface
'''
from abc import ABC
class I(ABC):
    def x1(self):
        pass
    def x2(self):
        pass
    
        
class II(I):
    def x1(self):
        print(10)
    def x2(self):
        print(20)
        
ob = II()
# ob.x1()
ob.x2()

'''Question = 
library management and banking applications '''

#ExceptionHandling
'''
Excepton occurs at runtime.
When we are getting any error at compilation tiem we say it as compilation error or syntax error.
In python all the exceptions are one one class.
When look at the exception handling tool like "try-except" or "try-finally" or "raise" or "try-else"  all are helping to identify the reason of the exception, at which the line the exception has occur So that programmer can take suitable correctiveness .
If we are not writting any exception handling tools then python vertual mechine will provide one exception handing tool for us which will the follwings 
1 - exception class
2 - line number 
3 - the reason of the exception
we can also provide exception handling tools 
 like try-except so that user can provide its own message for the reason of the exception.
 When we are having an exception but there is no exception handler tool then the following lines are not exicuted.
 If we provide the exception handing tool like try-except then any exception happends control stop and again start working after the except block.
 Follwing are the some the exceptions names 
    TypeError: Raised when an operation or function is applied to an object of inappropriate type.
    SyntaxError: Raised when there is a syntax error in the code.
    NameError: Raised when a local or global name is not found.
    IndexError: Raised when a sequence index is out of range.
    KeyError: Raised when a dictionary key is not found.
    ValueError: Raised when a function receives an argument of the correct type but with an invalid value.
    AttributeError: Raised when an attribute reference or assignment fails.
    ZeroDivisionError: Raised when division or modulo by zero occurs.
    ImportError: Raised when an import statement fails to find the module definition or when a from ... import statement encounters an error.
    
'''
#Without Try Except
# class Excp1():
#     def x1(self):
#         a = 10/0
#         print(a)
# ob = Excp1()
# ob.x1()
print("________________")
# -------------
# output: ZeroDivisionError: division by zero
            #   line 133, in <module>  ob.x1()
            #    line 130, in x1 a = 10/0
# ------------- 

# With Try Except  
class Excp2():
    def x1(self):
        try:
            a = 10/0
            print(a)
        except ZeroDivisionError as e:
            print(e)   
obj = Excp2()
obj.x1()
'''
advantage :
    we can write costomise message so that our message can be printed not the system define message 
    after try-except the follwing line are excuted 
    control flow :
                    1-10/0
                    2-obj is created inside pvm with some referance say ob 
                    3-pvm throught that ob for try-except (handel)-it written
                    4-it is mattching 
                    5-new referance name is assign
                    6-print(e)
                    it print the follwing 
                        the reason of the exception 
                        which method
                        line number
                        error class name etc. '''