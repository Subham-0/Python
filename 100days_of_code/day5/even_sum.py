target = int(input("Enter Number Between 0 and 1000"))
even_sum = 0 
for num in range(0,target,2):
    even_sum+=num+2
print(even_sum)
    
    
# or

even_num_sum=0
for number in range(0,target+1):
    if number%2 == 0:
        even_num_sum+=number
print(even_num_sum)
