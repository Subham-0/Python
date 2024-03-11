                # Dynamoc method dispatch or Runtime Polymerphism
# method overriding
class A8:
    def x1(self):
        print("1")
class B8(A8):
    def x1(self):
        print("2")
class C8(B8):
    def x1(self):
        print("3")       
ob = A8()
ob = B8()
ob.x1()
ob = C8()
ob.x1()
                    #Decorative model design partten
#question - There is a birthday celebratioin and following are the observation 
'''these is a base cake who price is 500 rupies
then going for designing and its price is 100
then going for writing price is 50 rupies 
chocko pasting is 100 rupies 
find the total of the cake if you are selecting all
if you leaving some item then what is the price
all the item name should be pass as user input
method name should be same and that is cost
Use dynamic method dispatch or runtime polymerphism '''

class basecake:
    def cost(self):
        return 500
class designing(basecake):
    def cost(self):
         return 100        
class writting(designing):
    def cost(self):
        return 50        
class pasting(writting):
    def cost(self):
        return 100        
ob = basecake()
cakeprice =  ob.cost()
ob = designing()
designingprice =  ob.cost()
ob = writting()
writtingprice =  ob.cost()
ob = pasting()
pastingprice =  ob.cost()

print("welocome my cake world!")
dis1 = input("whould you like buy a cake? y or n")
total = 0
if dis1.casefold() == "y":
    total = cakeprice
    print(f"the initial amount of the is {total}")
    dis2 = input("whould you like decorate your cake? y or n")
    if dis2.casefold() == "y":
        while(True):
            print("enter 1 for desigining\nenter 2 for writting\nenter 3 for pasting\nenter 4 for not chosing anything\n")
            enter_value = int(input())
            if enter_value == 1:
                  total+=designingprice
            elif enter_value == 2:
                 total+=writtingprice
            elif enter_value == 3:
                 total+=pastingprice
            elif enter_value == 4: 
                dis3 = input("Are you sure to not decorate anymore? y or n")
                if dis3.casefold() == "y":
                    break
print(f"Thank you for visiting\n Your total price is {total}")   
    
    

    
    
                    # Variables
#Follwing are the variables 
'''
1-static variable or class level variable:
    .there will be only one copy of that variable , any changes to that variavble will reflect everywhere in the class.in Python it is written below to the class and above to the constructor,method 
2-instance variable :
    .As many instance(obj) of a class that many are the instance variable,
    in python we can use self for instance variable and it is understood through out the class  
3-local variable:
    .the scope of the variable is with in the method or constructor because these variable is written with in that(method or constructor), it can not be access in other method
'''

class A:
    a=10
    b=20
    c=30
    d =0
    def x1(self):
        print(self.a) #instance
        ob = A()
        print(ob.b)
        print(A.c) # static
        print(self.d)  # scope local
        print(self.e)
       # print(ob.e) # after the it is so it is not printing
    def x2(self):
        d = 1000
        self.d = d
        self.e = 50
        # print(d)
ox = A()
ox.x2()
ox.x1()

                    #Abstract 
'''
abstract-class object can't not be created
A method should be abstract to make a class abstract
Abstract class can contain concrete method
As the abstract object can't be created then we have to make a child class of that abstract class and abstract method is overiding in the child class
'''
from abc import ABC
class AB(ABC):
    def x1(self):
        pass
    def x2(self):
        print(1)
        
class ABB(AB):
    def x1(self):
        print("good day")
    def x3(self):
        print("Thank U see you tommorow")
ob = ABB()
ob.x1()
ob.x2()
ob.x3()    
    
    