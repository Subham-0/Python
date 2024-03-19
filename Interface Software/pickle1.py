
            
import Emp,pickle
f = open("Emp.py","wb")
ob = Emp.Emp()
pickle.dump(ob,f)
print("dumped")
f.close()