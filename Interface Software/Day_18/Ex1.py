from threading import *
from time import *
class railway:
    def __init__(self,available):
        self.available = available
    def reserve(self,wanted):
        print("Available no of berths = " ,self.available)
        if(self.available>=wanted):
            name = current_thread().getName()
            print("%d berths allotted for %s"%(wanted,name))
            
            sleep(3)
            self.available -= wanted
            # self.available = self.available-wanted
        else:
            print("Sorry, no berths to allot")
obj = railway(2)
t1 = Thread(target=obj.reserve,args=(1,))
t2 = Thread(target=obj.reserve,args=(1,))
t3 = Thread(target=obj.reserve,args=(1,))
t1.setName('Subham')
t2.setName('gift')
t3.setName('mca')
t1.start()
t2.start()
t3.start()