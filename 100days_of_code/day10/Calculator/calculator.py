from art import logo
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
def calculator():
    print(logo)
    f_num = float(input("What's the first number?: "))
    for symobl in operation:
        print(symobl)

    should_continue = True
    while should_continue: 
        operation_symbol = input("Pick an opration: ")
        n_num = float(input("What's the next number?: "))
        calculation_fun =  operation[operation_symbol]

        ans =  calculation_fun(f_num,n_num)

        print(f"{f_num} {operation_symbol} {n_num} = {ans}")
        if input(f"Type 'y to continue calculation with the {ans}, or type 'n' to start a new calculation:") == 'y':
            f_num = ans
        else:
            should_continue=False
            calculator()

    
        
calculator()      

        