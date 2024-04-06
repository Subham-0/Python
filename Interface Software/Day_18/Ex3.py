
"""
In case of multithreading deadlock come when we are having two sycronization method
it means we are writting lock methods two times
In the conson method (book ticket and cancel ticket) we are using sycronize opration
In the both methods it was return l1.acquire and l1.release
similarly in other method l2.acquire and l2.release
if we write in the following way then deadlock situation will arise
In the first method we have written l2.acquire and l2.release
similarly in the second method we have also written l1.acquire and l2.release

* While we are in a sycronize method then not to call other cycronize mehod
"""

#dead lock of thrread
from threading import *

#take two locks
l1 = Lock()
l2 = Lock()

#creat a function for booking a ticket
def bookticker():
    l1.acquire()
    print('Bookticket locked train')
    print('Bookticket wants to lock on compartment')
    l2.acquire()
    print('Bookticket  locked compartment')
    l2.release()
    l1.release()
    print('Booking ticket done...')

#creat a function for camcelling a ticket
def cancelticket():
    l2.acquire()
    print('Cancelticket locked compsrtment')    
    print('Cancelticket wants to lock on train')
    l1.acquire()
    print('Cancelticket locked train')
    l1.release()    
    l2.release()
    print('Cancellation of ticket is done...') 

#Create two threads and run them
t1 = Thread(target=bookticker)   
t2 = Thread(target=cancelticket)
t1.start()   
t2.start()   