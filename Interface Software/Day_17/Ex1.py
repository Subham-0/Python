                # Multi-Threading
"""
    There are two type of Proccess
    1-Thread based multitasking
    2-Process based multitasking

Thread based multitasking:
    In case of thread based multitasking there are many process and at the same time all the process are working , but the origin of the process are from the main thread , which means from a program which contains the main thread and or child thread will come from the main thread
    
    Every programe is run by a frame which is called as the main thread
    
    Every main thread has a thread priority and by default it is 5.
    
    Every thread goes to a thread suduler which is the part of the opraation system and thread seduler look for the prority of the threads , as all the priroty are 5 then thread seduler goes for a first come first serve and allow the thread to work on the process
    
    Child thread and its life cycle:
        every main thread once it created autometically goes to a life cycle , so that thread can start and can run the main thread (there is no need for the life cycle of the main thread), where as child thread has the life cycle stage
        
        1-create the child thread
        2-after creation of the child thread then call a method call start so that the child thread is aivialable to thread suduler and call a method called run , so that thread seduler will allow a child
        
    How to create the child thred
        1-child thread can be created when we are extending  to a class called thread 
        2-thread belongs to a module called as a thread 
        3-once the thread is created by making the object of the class then we can  call to the start method which autometically call to run method
        4-every program is run by a main thread and if you want to know the thread name . That we can also find out the name of the main thread
    """
    
from threading import *
def show():
    print("Happy Utkal Divas")
   
for i in range(5):
     t= Thread(target=show)
     t.start()
     print(t)