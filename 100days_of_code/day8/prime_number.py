def prime_checker(number):
    count =0 
    for i in range(1,number+1):
        if number%i == 0:
            count+=1
    if count == 2:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
        
        
        
n = int(input())
prime_checker(number=n)
