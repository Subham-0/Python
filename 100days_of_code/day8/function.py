#function


def greet():
    print("Hello!")
    print("I am Subham")
    print("Now i am learning python from Udemy 100 days of python course.")

greet()

#function with input
def greeting(name):
    print("Hello!")
    print(f"I am {name}")
    
greeting("Subham")

#function with more than 1 input
def details(name,location):
    print(f"My full name is {name} and  i am from {location}")
    
details("Subham Dash","Odisha")
print("_______________________")
#position argument
details("Odisha","Subham Dash")
print("_______________________")
# to resolve this type of error use key argument
details(location="Odisha", name="Subham Dash")
