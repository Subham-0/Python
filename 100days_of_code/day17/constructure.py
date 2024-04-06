# it is a part of the blueprint that allows us to specify what should happen when a object is constructed and this is also known inprogramming as initializing an object 

#in python to create the constructor is by using a special function which is the __init__(self) function

#the init fuction every time called when you create a new object from this class

#self : it the actual object that being created or being initialized 
#you can pass as many parameter as you want when a object is created and when recived that in init function you can set the object's attributes

class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.name = user_name
        print("new user being created")
       
        self.follwers = 0   #set a default value of all user 
        self.follwing = 0 
        
    def follow(self,user):
        self.follwing +=1
        user.follwers +=1
        
       
user1 = User(1,"subham")
# user1.id = 1
# user1.name = "subham" 
print(user1.id)       
print(user1.name) 
# print(user1.follwers)      

user2 = User(2,"babulu")
# user2.id = 2
# user2.name = "babulu"
# user2.follwers = 45        
print(user2.id) 
print(user2.name)    
# print(user2.follwers) 

user1.follow(user2) 

print(user1.follwers) 
print(user1.follwing) 
print(user2.follwers) 
print(user2.follwing) 

print("--------------------------------")

user2.follow(user1) 

print(user1.follwers) 
print(user1.follwing) 
print(user2.follwers) 
print(user2.follwing)
       
      
