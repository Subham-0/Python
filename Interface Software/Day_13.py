'''
1-Write an example where list is used and add element to the list including objects then retrive the elements from the list?
2-create a tuple and add object to that tuple then tuple to be add as a key to the dictionary
3- write a example of dictionary where it is written inside the class and then make a list and a tuple as a static variable then called a method like x1 which will display the dictionary and retrive the list from that dictionary
4-write a example where all the concept are use like polymerphism , inheritance
5-write an example on interface
'''
#answer1
class a1:
    def fun(self):
        print("hello")
ob = a1()

lt1 = ["subahm",1,9.5,ob]
name = lt1[0]
print(name)
obj = lt1[3]
obj.fun()

#answer2
class a2:
    def fun1(self):
        print("tuple object")
ob = a2()
tup1 = (ob)
dic = {tup1:"tuple in dictionary"}
object = dic.keys()
# print(type(object))
#object.fun1()
t=tuple(dic.keys())
t1=t[0]
t1.fun1()

#answer3
class DTest:
    lt =[]
    tu = ()
    def x1(self):
        lt =[1,2,3]
        tu = (3,4,5)
        
        di = {
         "x1":lt,
         "x2":tu,
        }
        return di
      

