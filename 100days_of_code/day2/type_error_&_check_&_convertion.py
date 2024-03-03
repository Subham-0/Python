# print(len(123))
#TypeError: object of type 'int' has no len()

name = len(input("Enter your name"))
# print("your name has "+ name +" character") 
# TypeError: can only concatenate str (not "int") to str

print(type(name))

new_name = str(name)
print("your name has "+ new_name +" character") 

a = float(123)
print(type(a))

print(70+float("100.5"))
print(str(70)+str(100))
