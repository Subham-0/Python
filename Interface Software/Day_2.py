# LIST
'''This datatype has the following properties:'''
#  It is a collection type datatype, which means any type of object can be kept inside a list.
# This datatype can contain multiple values.
# This datatype is mutable.
# Addition and deletion can be done using index numbers.
# A list can be created using the list method.
# It is kept inside square brackets.
# Forward indexing and backward indexing are possible.
# Forward slicing and backward slicing are possible.
# Concatenation and multiplication are possible.

# Not possible in a list:
# Immutable - not possible
# Duplicate values - not possible
# Unique elements - not possible

#Python lists are mutable, can contain duplicate values, and do not inherently enforce unique elements.

#Flow to create an Object in python




from turtle import lt


class Ex1:
    def x1(self):
        print(50)
    def x2(self):
        print(150)
obj = Ex1()
obj.x1()
obj.x2()

lt1= [1,3,5,True,"SD"]
print(lt1)
print(type(lt1))
print(id(lt1))

#for indexing start from 0
#for lenght start from 1

#Forward Slicing
print(lt1[3])
print(lt1[2:4]) # index2 to index4-1 [5,True]

#Backward Slicing
print(lt1[-3])
print(lt1[-3:-1]) # index-3 to index-1-1 [5,True]

#slicing in list return values in list
a = lt1[1:4]
print(a)
print(type(a))

print(lt1[2:]) #index4 to last
print(lt1[:3]) #index0 to index3

# Example_1
lt1 = [1,3.5,True,"pk",1] 
print(lt1[1::1])
# if you want to print in a sequence 
print(lt1[1::2])
print(lt1[::2])

#Multiplication and concatination
lt1 = ["pk",5]
lt2 = [1,3]
lt3 = lt1+lt2
print(lt3)
print(lt2*3)

#Some poupular Methods in list
# append
# clear
# copy
# count
# extend
# index
# insert
# pop
# remove
# reverse
# sort

lt1 = [1,'hello',3,4,5,1,3]

print(lt1[1])
print(lt1[5])

#add atleast two type of datatype 
# Argument of type "list[int]" cannot be assigned to parameter "__object" of type "int" in function "append"
lt2 = [3,6,7,3,5]
lt1.append(lt2)
lt3 = lt1
print(lt3)

a = lt3.count(3)
print(a)

lt4 = [23,'Subham',False]
lt5 = lt4.copy()
print(lt5)

lt2.extend([1,7,9])
lt7 = lt2
print(lt7)

# list.index(value, start, end)
lt2 = [3,1,6,7,3,5]
# print(lt2.index(1,4)) #error after index 4 the value don't exist
print(lt2.index(3,1)) 
# return in which index the value
print(lt2.index(6,2,3)) 
#return index of the value 6 if exist in between index2 to index3

lt2.insert(2,20)
print(lt2)

lt2.pop(3)
print(lt2)

lt2.reverse()
print(lt2)

lt2.remove(20)
print(lt2)

lt2.sort()
print(lt2)


lt2.clear()
print(lt2)

# Question-1 Create a list which contains 2 list, cotaining the value Quantity and Price . It comes as a input and kept inside the list.wchich is kept inside the main list 
# Find the grand total price?



input_quantity=int(input("enter the quantity"))
input_price=eval(input("enter the price"))
list1 = []
list1.insert(0,input_quantity)
list1.insert(1,input_price)
print(list1)
list_total = list1[0]*list1[1]
print(list_total)


# Question-2 List contains one obj now get the object from the list and then call the method


class MyClass:
    
    def say_hello(self):
        print("Hello Sir!")

obj = MyClass()
my_list = [obj]
obj_from_list = my_list[0]
obj_from_list.say_hello()

# Question 3
# In our MCA we are 4 semester . 
# Find even semester marks only as well as odd semester marks also list contain all 4 semester mark.
# Find the average of all 4 semester
# Max_mark in which semester and Min_mark in which semester(condition: only list will use)

lst1 = [8.2,8.74,7.9,8.8]
print(lst1[::2]) #odd sem
print(lst1[1::2]) #even sem
print(sum(lst1[::1])/4) #avg of total sem
print(max(lst1)) #max mark
print(min(lst1)) #min mark
print(lst1.index(max(lst1))+1) #max mark in which sem 
print(lst1.index(min(lst1))+1) #min mark in which sem 
