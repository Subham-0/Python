
"""Q - write a file whose name is 'ABC.txt' that file contain about your in formation 
    maximun 10 lines 
    So one line must contain mark = 95
    now find your name from that file.how many times 'the' repeted
    find your marks
    biodata and design is yours"""



file = open("resume.txt",'r')
list1 = file.readlines()
print(list1)

st = list1[0]
print(st)

st1 = st[3:7]+":"+st[11:]
print(st1)
mark = list1[9]
print(mark)
mark_data = mark[3:7]+":"+mark[11:13]
print(mark_data)
st2 = str(list1)
print(st2.count("My"))

   
# listdir(path)
'''this method tells about how many file are there in the director and that is to be store in list'''

import os
path = r"C:\Users\HP\Desktop\PYTHON\Python"
s1 = os.listdir(path)
# print(s1)
lt = []
lt2 = []
for x in s1:
    if(x.endswith(".py")):
        lt.append(x)
    if(x.startswith("Emp")):
        lt2.append(x)
        
print(lt)
print(lt2)

# Date and time
'''returns a time  tuple ''' 
import time;
print(time.localtime())
a = time.localtime(time.time())
print(a)

#returns the formatted time
b = time.asctime(time.localtime())
s = b.split()
print(s)
ss = s[3]
print(ss)
print(ss[:2].rstrip(":"))

d= s[2]
m= s[1]
y= s[4]
print(d+'/'+m+'/'+y)

 