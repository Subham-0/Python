from threading import *
import time
def show():
    print("this is 1st thread")
def greet():
    print("hello good morning") 
     
for i in range(5):
    t = Thread(target=show)
    t.start() 
    print(t)

       
for i in range(4):
    t1 = Thread(target=greet)
    t1.start()  
    print(t1)  