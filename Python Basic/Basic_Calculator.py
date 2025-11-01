# Basic Calculator in Python by using the arithematic operators.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Sum:", a + b)
elif op == "-":
    print("Difference:", a - b)
elif op == "*":
    print("Product:", a * b)
elif op == "/":
    if b != 0:
        print("Division:", a / b)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator!")
print("THANK YOU !!!!!!")