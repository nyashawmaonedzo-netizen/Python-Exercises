print("Simple Calculator: choose an operation and enter two numbers.")

operator = input("Enter operator (+, -, *, /): ")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

if operator == '+':
    output = a + b
elif operator == '-':
    output = a - b
elif operator == '*':
    output = a * b
elif operator == '/':
    if b != 0:
        output = a / b
    else:
        print("Cannot divide by zero.")
        output = None
else:
    print("Unsupported operator.")
    output = None

if output is not None:
    print(f"The result of {a} {operator} {b} is {output}")
