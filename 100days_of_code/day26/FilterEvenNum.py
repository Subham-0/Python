list_of_string =  input().split(',')
numbers = [int(num) for num in list_of_string ]
result = [num for num in numbers if num%2==0]
print(result)