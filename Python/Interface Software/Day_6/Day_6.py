                # Inheritance
# five type of inheritance

# single inheritance

class A:
    def x1(self):
        print("good moring")
class B(A):
    def x2(self):
        print("happy sunday")       
ob = B()
ob.x1()
ob.x2()

#multilevel inheritance

class A1:
    def x1(self):
        print("good moring")
class B1(A1):
    def x2(self):
        print("happy sunday")
class C1(B1):
    def x3(self):
        print("good afternoon")       
ob = C1()
ob.x1()
ob.x2()
ob.x3()

#hierarchical Inheritance

class A2:
    def x1(self):
        print("base fuction")
class B2(A2):
    def x2(self):
        print("child function")
class C2(A2):
    def x3(self):
        print("also a child function")  
        
ob = C2()
ob.x1()
# ob.x2()
ob.x3()     

ob = B2()
ob.x1() 
ob.x2()
# ob.x3()  
        
#Multiple Inheritance

class A3:
    def x1(self):
        print("MI base1")
class B3:
    def x2(self):
        print("MI base2")
class C3(A3,B3):
    def x3(self):
        print("MI child")

ob  = C3()
ob.x1()
ob.x2()
ob.x3()

#hybrid Inheritance
class A4:
    def x1(self):
        print("HI base1")
class B4(A4):
    def x2(self):
        print("HI child1")
class C4(A4):
    def x3(self):
        print("HI child1")
class D4(B4,C4):
    def x4(self):
        print("HI child1--child1")
ob = D4()
ob.x1()
ob.x2()
ob.x3()
ob.x4()

            #Constructor
class A5:
    def __init__(self):
        print("good morning")
ob = A5()


class A6:
    def __init__(self):
        print("good morning")
class B6(A6):
    def __init__(self):
       
        print("good noon")
class C6(B6):
    def __init__(self):
        super().__init__()
        print("good night")
ob = C6()


class A7:
    def __init__(self, name=None):
        if name is None:
            print("good morning")
        else:
            print(f"good morning, my name is {name}")

# Creating instances with different constructor signatures
ob1 = A7()  # This will run the non-parameterized version
ob2 = A7("Alice") 

#polymerphism
# method overloading and conststructor are not allow


# method overriding
class A8:
    def x1(self):
        print("good moringgg")
class B8(A8):
    def x1(self):
        super().x1()
        print("happy sunday")
class C8(B8):
    def x1(self):
        super().x1()
        print("good afternoon")       
ob = C8()
ob.x1()

# ob = A8()
# ob.x1()
# ob =B8()
# ob.x1()


    
