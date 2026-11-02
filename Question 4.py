
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter an operation (+, -, *, /): ")


result = None
is_valid = True

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        is_valid = False
    else:
        result = num1 / num2
else:
    print("Error: Invalid operation symbol.")
    is_valid = False

if is_valid:
    print(f"The result is: {result}")
