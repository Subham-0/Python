with open("./file1.txt") as file1_data:
    data1 = file1_data.readlines()
      
with open("./file2.txt") as file2_data:
    data2 = file2_data.readlines()
  
result = [int(num) for num in data1 if num in data2]
print(result)