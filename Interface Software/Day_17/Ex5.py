# task = prepare a tea by us and following are the task 
# 1- switch on the stove
# 2-put the boiling pot and the water to hot for two minutes 
# 3-put the dust and sugar and boild for 2minutes
# 4-then filter it
# write the example using class and run method

from threading import *
from time import *
class TeaMaking:
    def prepare_tea(self):
        self.step1()
        self.step2()
        self.step3()
    def step1(self):
        print("stove to on-boil milk and water for five minutes",end="  ")
        sleep(3)
        print("Step one done")
    def step2(self):
        print("Put sugar and teadust",end=" ")
        sleep(2)
        print("Step two done")
    def step3(self):
        print("Filter and surve",end=" ")
        sleep(4)
        print("Step three done")
        
obj = TeaMaking()
t = Thread(target=obj.prepare_tea)
t.start()
t.join()

        # OR

# from threading import *
# from time import *
# class TeaMaking (Thread):
#     def run(self):
#         self.step1()
#         self.step2()
#         self.step3()
#     def step1(self):
#         print("stove to on-boil milk and water for five minutes",end="  ")
#         sleep(3)
#         print("Step one done")
#     def step2(self):
#         print("Put sugar and teadust",end=" ")
#         sleep(2)
#         print("Step two done")
#     def step3(self):
#         print("Filter and surve",end=" ")
#         sleep(4)
#         print("Step three done")
        
# obj = TeaMaking()

# obj.start()
