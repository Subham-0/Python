def add(*args):
    # print(args[1])
    sum = 0
    for n in args:
        sum+=n
    return sum

print(add(4,7))

def multiplication(*argu):
    mul = 1
    for i in argu:
        mul*=i
    return mul

def calculate(n,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
        
    print(kwargs["add"])
    
    n += kwargs["add"]
    n *= kwargs["multi"]
    print(n)

calculate(2,add=add(3,7),multi=multiplication(5,8,9))

# creating own class to use optional arguments

class Car:
    def __init__(self,**kw):
       
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        
my_car1 = Car(make="Nissan",model="GT-R")
my_car2 = Car(make="Suzuki")

print(my_car1.model)
print(my_car1.make)

print(my_car2.make)
print(my_car2.model)

#

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
