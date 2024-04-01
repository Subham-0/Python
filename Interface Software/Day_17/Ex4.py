from threading import *
from time import *
class mythread (Thread):
    def run(self):
        for i in range(1,6):
            print(i)
            sleep(2)
t1 = mythread()
print(t1)
t1.start()
t1.join()
print(t1)