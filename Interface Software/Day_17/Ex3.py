# child thread calling to parameterized method
from threading import Thread
def show(str):
    print(str)
for i in range(5):
    t = Thread(target=show,args=("hello",))
    t.start()