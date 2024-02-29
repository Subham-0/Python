# History of Python

# It was discovered by Guido van Rossum.
# He is from Holland (Netherlands).
# It was discovered in the year 1990-1991.
# It was conceived around the 1980s.
# It is an object-oriented language.
# At the beginning of the development of Python, it was experimented with on another OS like Amoeba.
# The name "Python" was derived from the BBC serial "Monty Python's Flying Circus."
# Python 2.0 was released on October 16, 2000.
# The current version is 3.12.
# Version 1.0 came with Exception handling, and in 2.0, it came with garbage collection (GC) and memory management.
# The major breakthrough came in 3.0 after a long period of testing, and it was released on December 8, 2008.
# After the rise of the 5V principles (velocity, variety, volume, value, veracity) in data flow, the volume of data also became significant.
# Python was developed to determine where algorithms are used and for decision-making purposes.
# Like other languages such as Java and .NET, Python is also an object-oriented language. However, Java does not use the Scientific algorithm model.
# Python was developed at CWI (Centrum Wiskunde en Informatica).

# Here are the advantages of Python:

# Simplicity: Python is known for its simplicity and readability, making it easier to learn and write code.

# Object-Oriented: Python supports object-oriented programming (OOP) principles, allowing for the creation of reusable and modular code.

# Robust and Platform Independent: Python programs can run on various platforms without any modifications. It offers robust error handling and testing capabilities.

# Multithreaded: Python supports multithreading, allowing programs to perform multiple tasks concurrently.

# GUI Development: Python provides libraries like Tkinter, PyQt, and wxPython for developing graphical user interfaces (GUIs) easily.

# Database Connectivity: Python offers standard libraries such as SQLite3 for connecting to and working with databases like MySQL, PostgreSQL, Oracle, etc.

# High-Level Language: Python's high-level nature means that it abstracts many complex details, making it easier to focus on solving problems.

# Dynamically Typed: Python is dynamically typed, meaning that you don't need to specify variable types. The interpreter assigns types during runtime, making development faster.

# Compiled and Interpreted: Python code can be compiled into bytecode (.pyc) files for faster execution, and it can also be interpreted directly, providing flexibility for different use cases.

# Garbage Collection: Python automatically manages memory allocation and deallocation, making memory management easier for developers.

# Open Source and Free: Python is an open-source language with a large community contributing to its development. This means that it is free to use and distribute.

# Rich Libraries: Python has a vast standard library and numerous third-party libraries for various tasks, including data science, web development, machine learning, and more.

# Data Science and Visualization: Python is widely used in data science due to libraries like NumPy, Pandas, Matplotlib, and Seaborn. These libraries make data manipulation, analysis, and visualization straightforward.

# Mobile Communication: Python can be used for mobile app development using frameworks like Kivy and BeeWare.

# Web Development: Python is used for web development with frameworks like Django, Flask, and Falcon, making it easy to create powerful and scalable web applications.

# Portability: Python code can be easily ported across different platforms, ensuring compatibility and flexibility.

# Community Support: Python has a large and active community, providing support, tutorials, and resources for developers.

# Ease of Use for Machine Learning: Python is the language of choice for many machine learning and AI applications due to libraries like TensorFlow, scikit-learn, and PyTorch.

# Versatility: Python's versatility allows it to be used in a wide range of applications, from scripting and automation to web development, scientific computing, and more.

# Ease of Integration: Python can easily integrate with other languages like C/C++, Java, and .NET, expanding its capabilities and interoperability.


# Examples-1
# print(Hello) //not correct
print('Hello')
print("Hello")
print("Hello");
# print("Hello");;  not correct

# Examples-2
#single line comment
'''multiline comment'''
"""multiline comment"""
# find the diffence between above two ways of comment line ?
#  Ans----> ''' ... ''': Treated as a multi-line string literal, unless assigned to a variable, in which case it is a docstring.
#           """ ... """: Treated as a multi-line comment and ignored by the interpreter.

# Example-3
# Indentation
class Ex1:
    def x1(self):
        print("hello")

obj = Ex1();
obj.x1();


num = 30;
if(num>40):
    print("big")
elif(num % 4 == 0):
    print("divisible by 4 and lessthan 40")
else:
    print("Smaller than 40 not divisible by 4")


def x1():
    try:
        a = 10/0
    except ZeroDivisionError as e:
        print("Error:", e)

# Call the function to test
x1()


import keyword 
print(keyword.kwlist)
#   ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']  

# 'False', 'None', 'True' these are in uppercase and all are lowercase

# String Declaration
s1='Subham'
s2="Dash"
s3='''Subham Dash'''
print(s1)
print(s2)
print(s3)
# what are diffence between above three ways of String Declaration?
s5 = '''He said, "Hello"'''
s6 = """She said, 'Hi'"""

# Single Quotes (') and Double Quotes ("): Basic string declaration, interchangeable, based on personal preference or string content.

# Triple Quotes (''' or """): Useful for multi-line strings, docstrings, strings with both single and double quotes, and strings that need to span across multiple lines without using escape characters.

# Taking the vaues fron user input
a=input("Enter the first value")
b=input('enter the second value')
print(a+b)
print(type(a))   
# it gives the datatype of a
print(type(b))
#go for type case
a1 = int(a)
print(type(a1))
b1 = int(b)
print(type(b1))
print(a1+b1)
print(id(a1))
#Hashcode of that value
print(id(b1))

# User input another way
a= eval(input("enter the firstNo"))
b= eval(input("enter the secondNo"))
print(type(a))
print(a+b)
#this is dynamic typecasting (string to int or float)
 

