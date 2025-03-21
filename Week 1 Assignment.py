# Basic Calculator Program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        exit()  
    result = num1 / num2
else:
    print("Invalid operation. Please use +, -, *, or /.")
    exit() 

# S the result in the required format (e.g., 10 + 5 = 15)
print(f"{num1} {operation} {num2} = {result}")