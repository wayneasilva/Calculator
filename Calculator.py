class calculator:

    def addition(x,y):
        added = x + y
        print(added)

    def subtraction(x,y):
        sub = x - y
        print(sub)

    def multiplication(x,y):
        mult = x * y
        print (mult)

    def division(x,y):
        div = x / y
        print(div)

x = int(input("Type first number \n"))
y = int(input("Type second number \n"))

print(x,y)

def calculate():
    arith_type = int(input("Now type the corresponding number for the type of operation you would like "
                       "\n 1 = Add \n 2 = Subtract \n 3 = Multiply \n 4 = Divide \n"))
    print(arith_type)

    if arith_type == 1:
        calculator.addition(x,y)

    elif arith_type == 2:
        calculator.subtraction(x,y)

    elif arith_type == 3:
        calculator.multiplication(x,y)

    elif arith_type == 4:
        calculator.division(x,y)

    else:
        calculate()

calculate()