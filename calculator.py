OneNum = int(input("1. num: "))

Calc = input("Type of Calculation (+, -, *, /): ")

TwoNum = int(input("2. num: "))

def add (x, y):
    z = x + y
    return z

def subtract (x, y):
    z = x - y
    return z

def multiply (x, y):
    z = x * y
    return z

def divide (x, y):
    z = x / y
    return z

if Calc == "+":
    print(add(OneNum, TwoNum))

elif Calc == "-":
    print(subtract(OneNum, TwoNum))

elif Calc == "*":
    print(multiply(OneNum, TwoNum))

else:
    print(divide(OneNum, TwoNum))
