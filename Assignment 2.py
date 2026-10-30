# A programm to make a simple calculater

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Select an operation (+, -, *, /, **, %) ")
if operation == "+":
    print(f"The sum is {num1 + num2}")

elif operation == "-":
    print(f"The difference is {num1 - num2}")

elif operation == "*":
    print(f"The product is {num2 * num1}")

elif operation == "/":
    print(f"The quotient is {num1 / num2}")

elif operation == "**":
    print(f"The exponent is {num1 ** num2}")

elif operation == "%":
    print(f"The modulus is {num1 % num2}")

else:
    print("Invalid operation entered")