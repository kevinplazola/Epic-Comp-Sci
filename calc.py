def numbers(x, y):
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    return x, y

def operation():
    op = input("Enter the operation (+, -, *, /): ")
    return op

x, y = numbers(0, 0)
op = operation()

if op == "+":
    result = x + y
    print(f"The result of {x} + {y} is: {result}")
elif op == "-":
    result = x - y
    print(f"The result of {x} - {y} is: {result}")
elif op == "*":
    result = x * y
    print(f"The result of {x} * {y} is: {result}")
elif op == "/":
    if y != 0:
        result = x / y
        print(f"The result of {x} / {y} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /.")