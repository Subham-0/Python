"""the above example without Synchronization
to synchronize the thread we have to use three methods 
       1-Lock()
       2-acquire()
       3-release()"""
        
from threading import Thread, Lock , current_thread
from time import sleep

class Railway:
    def __init__(self, available):
        self.available = available
        self.l = Lock()
    
    def reserve(self, wanted):
        self.l.acquire()
        print("Available no of berths =", self.available)
        if self.available >= wanted:
            name = current_thread().name
            print("%d berths allotted for %s" % (wanted, name))
            sleep(3)
            self.available -= wanted
        else:
            print("Sorry, no berths to allot")
        self.l.release()

obj = Railway(2)
t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))
t3 = Thread(target=obj.reserve, args=(1,))

t1.setName('Subham')
t2.setName('gift')
t3.setName('mca')

t1.start()
t2.start()
t3.start()
