
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


#               Use of sleep method
#print by sleep method 
'''
sleep method belong to class called time and throught that method we can pass the integer value which says that much of time the processor sleeps then again time slap is over then process start again from there where it has been stop or paused

We have to import time to get the sleep method 
'''
# import time
# for i in range(0,5):
#     print(i)
#     time.sleep(2)
    
    
#To print date and time
#here we are using a packet called datetime then we have using a function now which give year month data and hour minitues second 
# then we are using a function todate do that the current day can be display
import datetime

print(datetime.datetime.now())
print(datetime.datetime.today())

# if we want to set date then called to the constroctor of datatime then pass the arguments
d = datetime.date(2025,2,24)
print(d)

#timestamp
#here we have to pass the  second then it will give year ,month from a date ,here we are using a function called as fromtimestamp to that we can pass the second through that

from datetime import date
ts = date.fromtimestamp(993456744)
print(ts)

#here we are usung a functionn called as fron


#class calender
'''in the following ecxample we are using calender class to get the calender of the month
month method takes two argument year and month'''
import calendar
cal = calendar.month(2024,3)

print(cal)

#to find the calender of the total year
import calendar
year = int(input("enter the year"))

s = calendar.prcal(year)

print(s)

print(calendar.calendar(year,4,1,8,2))

#Difference between two timedelta object
from datetime import timedelta
t1 = timedelta(weeks=2,days=5,hours=12,seconds=34)
t2 = timedelta(weeks=1,days=4,hours=11,minutes=4,seconds=54)
t3 = t1 - t2
print("t3 - ",t3)

from datetime import datetime

# datetime(year, month, day)
a = datetime(2022, 12, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)

from datetime import time

a = time(11, 34, 56)

print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56)
print(b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print(c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print(d)

from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
 