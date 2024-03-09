                    #Function or Method
'''In python can be written outside the class or inside the class.
It can be parameteries or paramerter less.'''

#Function without class



def x1():
    print("Hello!")
    
def x2(a,b):
    print(a+b)
    
x1()
x2(1,4)

#Q1- Write a class make an object of that class and then pass that object through a function say x1.
# then form x1 function called x2 where we have pass that through list . find the total and grand total.

class Ex1:
    def x1(self):
        return 5000
ob = Ex1()
lt = [ob,]
# print(lt)
def x2(object):
    print(object[0].x1())
    
x2(lt)

                # class object and constructure

class Ex2:
    def x2(self):
        print("SD")
ob = Ex2()
ob.x2()

#default constructure
class Ex4:
    def __init__(self):
        print("con is called")
    def x4(self):
      print("tommorrow is java class")
ob = Ex4()
ob.x4()  

#parameteies constructer 

class Ex5:
    def __init__(self,a,b):
        print("con is called")
        print(a+b)
    def x4(self):
      print("tommorrow is java class")
ob = Ex5(100,200)
ob.x4()    

# default and parameter constructor
class Ex3:
    # def __init__(self):       # Constructor overloding and method overling is not allow in python 
    #     print("Hello")
    def __init__(self,a,b):
        print("con is called")
        print(a+b)
    def x4(self):
      print("tommorrow is java class")
ob = Ex3(100,200)
# ob = Ex3()
ob.x4() 

