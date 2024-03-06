# TUPLE
'''It is like a list.
It is also a collection type datatype, which means a collection of objects.
It can contain heterogeneous elements.
It supports forward indexing as well as backward indexing.
It supports forward slicing and backward slicing.
It also supports multiplication and concatenation.
It is immutable.
Duplicate values are allowed.
It is denoted by parentheses ( ).'''

from operator import index


class Ex1:
    def x1(self):
        print("hello!")
ob = Ex1()

tup1 = (1,2,3.4,"SD",True,ob)
print(tup1)
tup1[5].x1()

#indexing(forward and backward )
print(tup1[1])
print(tup1[-3])
#slicing(forward and backward )
print(tup1[:2])
print(tup1[-3:-1])
# concatination and multiplication 
t1 = (1,2)
t2 = (3,4)
print(t1+t2)
print(t2*3)

#methods
#len()
p1 = (1,2,3.4,True,1,False)
print(len(p1))
# count()
print(t1.count(1))
# index()
print(index(2))
# sorted()
p2 = (1,2,3,5,9,7)
print(sorted(p2))
# min()
print(min(p1))
# max()
print(max(p1))
# any()
print(any(p1))
# all()
print(any(p1))

             # SET
'''
1- This datatype does not support forward indexing and backward indexing.
This datatype does not support forward slicing and backward slicing.
It also does not support concatenation and multiplication.
It is written within curly braces {}.
It contains only unique elements (no duplicates).
If duplicate elements are present, only one element will be visible.
It can contain heterogeneous elements.
s2 = {"a", "x", "b", 1, "a"}
print(s2)
Insertion order is not preserved.
'''


# methods
s1 = {1,2,3,4}
s2 = {1,3,4,5}
s3 = {2,3,4,6}
s3.add(0)
print(s3)
# s3.remove(5)      
s3.remove(0) 
print(s3)

s3.discard(5)       
print(s3)


s4 = s3.copy()
print(s4)

s2.pop()
print(s2)

s3.clear()
print(s3)

s1 = {1,2,3,4}
s2 = {1,3,4,5}
s3 = {2,3,4,6}

print(s1.union(s2,s3))
print(s1.difference(s2))
print(s1.difference(s3))
print(s1.intersection(s3))

            # DICTIONARIES
'''In Python, a dictionary is a datatype.
It contains key-value pairs.
Keys are immutable, which can be a string or tuple.
Values can be any object.
Keys are unique - if duplicate keys are present, only one is visible.
Values can be multiple and of any collection-type object.
It is written within curly braces {}.

dic1 = {1: 2, 4: 5, "a": "Ram", (1, 2): "sam"}

'''
