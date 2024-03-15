#try--multiple except
'''
In the following example we are having all try followed by mutile except.
It can be used one exception is not matching then it look for the second exception from the multiple exception list which we have written. 
If any of the exception is not matching then python vertual mechine will gives its message.
'''
class Excep3:
    def  x1(self):
        try:
            b=int(input("Enter the Value"))
            print(1)
            a=10/b
            print(a)
        except NameError as e:
            print(e)
        except ZeroDivisionError as e:
            print("Error-0")
            print("Please don't enter 0 as 0.0 as a divisor")
        except ValueError as e:
            print("please don't pass any string ot float ")
ob = Excep3()
ob.x1()

#try-finally
'''
We can also write finally along with try block.
Finally block can be written along with try and except also.
This block is excuted at any cost which means wheater we are having any exception or not this block is excuted at any cost.

'''
class Excep4:
    def x1(self):
        try:
            print("GM")
        except NameError as e:
            print(1)
        finally:
            print(2)
    def x2(self):
        try:
            a = 10/0
        # finally:
        #     print(4)
        # except ZeroDivisionError as e:
        #     print(3)
        except ZeroDivisionError as e:
            print(3)
        finally:
            print(4)
    def x3(self):
        try:
            return
        except TypeError as e:
            print(5)
        finally:
            print(6)
ob =  Excep4()

ob.x1()
ob.x2()
# try:
#     ob.x2()
# except ZeroDivisionError as e:
#     print(3)
ob.x3()

# raise
'''
This keyword is used for exception handeling for user define exception.
In all the previos examples exception names are system define like ZeroDivision error , NameError etc where the reason is also python specific.
If we want our exception name is our's and resason is our's then we can use user defind exception for that.
'''
'''
Steps to write :
    1-User define exception class should extends to a class called exception.
    2-Inside that class write the methods where the defination is the reason of the exception
    3-Now the suitable code so the exception will occur and that exception will be raised(exception will be through).
    4-Once it is raised then it is to be handeled by user defind exception.
'''
class LowSalaryError(Exception):
    def show(self):
        print("You are getting less Salary")
        
class LowAttendanceError(Exception):
    def show(self):
        print("You are very low Attendance")
        
class userExcetion:
    sal = eval(input("enter the salary"))
    if(sal>10000):
            print("salary is ok")
    else:
         try:
            ob = LowSalaryError()
            raise ob
         except LowSalaryError as e:
            e.show() 
                 
    attendance = eval(input("enter your attendendances "))
    if(attendance>80):
        print("you are able to apper the exam")
    else:
        try:
            ob = LowAttendanceError()
            raise ob
        except LowAttendanceError as e:
            e.show()
            
# try-except-else
'''
else is a block that can be written along with try and except .
when there is an exception then we find there an except block.
when there is no exception then we find else block is excuted.
'''
class Excep6:
    def x1(self):
        try:
            x = int(input("Please enter a number: "))
        except ValueError:
            print("Oops! That was not a valid number.")
        else:
             print("You entered:", x)
        finally:
            print("all time printing")
obj = Excep6()
obj.x1()