from art import logo
print(logo)

# f_num = int(input("What's the first number?: "))
# op = ['+','-','*','/']
# for one_op in op:
#     print(one_op)
# choose_op = input("Pick an operation: ")
# n_num = int(input("What's the next number?: "))
# def add():
#     return f_num+n_num
# def sub():
#     return f_num-n_num
# def mult():
#     return f_num*n_num
# def div():
#     return f_num/n_num
   
# if choose_op == '+':
#      print(add())
# elif choose_op == '-':
#     print(sub())
# elif choose_op == '*':
#     print(mult())
# elif choose_op == '/':
#     print(div())

                    # OR
                    
f_num = int(input("What's the first number?: "))
n_num = int(input("What's the next number?: "))

def add(f_num,n_num):
    return f_num+n_num
def sub(f_num,n_num):
    return f_num-n_num
def mult(f_num,n_num):
    return f_num*n_num
def div(f_num,n_num):
    return f_num/n_num
   

operation = {
    '+':add,
    '-':sub,
    '*':mult,
    '/':div
}

for symobl in operation:
    print(symobl)
    
    
operation_symbol = input("Pick an opration symbol from the line above: ")
calculation_fun =  operation[operation_symbol]

ans =  calculation_fun(f_num,n_num)

print(f"{f_num} {operation_symbol} {n_num} = {ans}")

# operation_symbol2 = input("Pick an opration symbol again: ")

# calculation_fun =  operation[operation_symbol2]

# t_num = int(input("What's the next number?: "))

# ans2 =calculation_fun(ans,t_num)

# print(f"{ans} {operation_symbol2} {t_num} = {ans2}")
