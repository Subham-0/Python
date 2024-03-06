                #STRING HANDELING

''' 
1- It is a combination of collection of character. 
2- It is immutable. (Value can not be change)
3- Forward indexing and Backward indexing possible.
4- Forward slicing  and Backward slicing possible.
5- Concatination and Multiplication possible.
'''




st1 = "I am a developer"
st2 = "I am a developer"
st3 = "I am a developer"
print(id(st1))
print(id(st2))
print(id(st3))
st4 = "I am a Developer"
print(id(st4))
'''In string handeling of python, when we are declaring a string, it's store in a string constant pull area
If the contain are same then it will give the same id to all the reference
If any change in the string (here we are just changing the character ) then we find the id will be changed
(it is with respect to 3.7 of python version)
This is a rule by python , but it may give different answer in different IDE'''



st1 = "My Name is Subham  Dash"
#Forward indexing and slicing
print(st1[0])           #M
print(st1[:7])          #My Name
print(st1[0:])          #My Name is Subham  Dash
print(st1[3:17])        #Name is Subham
print(st1[3::8])        #NSD


#Backward indexing and slicing
print(st1[-1])          #h
print(st1[:-4])         #My Name is Subham
print(st1[-4:])         #Dash
print(st1[-15:-6])      #is Subham
print(st1[::-1])        #hsaD  mahbuS si emaN yM   (mirror image)


#Concatination and Multiplication
st2 = [1,2,3]
st3 = ['A','B','C']
print(st2+st3)
print(st2*3)

# Function in String
print(len(st1))
print(st1.capitalize())     #Converts the first character to upper case
print(st1.title())          #Converts the first character of each word to upper case
print(st1.casefold())       #Converts string into lower case
st2 = "Subham"
print(st2.center(10,"✓"))   #center align the string, using a specified character (space is default) as the fill character.
st3 = "i love apple apple and apple above the all fruits"
print(st3.count("apple"))       #returns the number of times a specified value appears in the string.
print(st3.count("apple",4,20))  #string.count(value, start, end)

print(st3.endswith("fruits"))   #Returns true if the string ends with the specified value
print(st3.endswith("and",10,22))
print(st3.startswith("i"))

print(st3.upper())
print(st3.lower())

txt = "S\tu\tb\th\ta\tm"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))        #each tab have 1 space
print(txt.expandtabs(4))        ##each tab have 3 space
print(txt.expandtabs(10))       ##each tab have 9 space

print(st3.find("above"))        #return start index of finding element

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
print(txt.find("q"))     
# print(txt.index("q"))         #If the value is not found, the find() method returns -1, but the index() method will raise an exception

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
# he format() method formats the specified value(s) and insert them inside the string's placeholder.
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)

# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
#Join all items in a tuple into a string, using a hash character as separator:

txt = "welcome to the jungle"      
x = txt.split()
print(x)                                

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")  #of all fruits banana is my favorite