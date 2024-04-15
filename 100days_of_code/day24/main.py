# file = open("my_file.txt")

# contents = file.read()
# print(contents)

# file.close()

# instaded of manually close the open file we can write like this to close the file autometically
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    
# with open("/Users/HP/Desktop/PYTHON/Python/100days_of_code/day24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
    

    
#remove the previous data write new
with open("my_file.txt", mode='w') as file:
    file.write("\nNew text added")

#write new data with the existing data    
with open("my_file.txt", mode='a') as file:
    file.write("\nNew text added")