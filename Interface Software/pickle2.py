import Emp,pickle
f = open("Emp.py","rb")
obj = pickle.load(f)
obj.show()
obj.display()