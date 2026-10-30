# a program to find the largest among three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Solution 1
# if num1 > num2 and num1 > num3:
#     print(f"The largest number is {num1}")

# elif num2 > num1 and num2 > num3:
#     print(f"The largest number is {num2}")

# else:
#     print(f"The largest number is {num3}")

# Solution 2

x = max(num1, num2, num3)
print("The largest number is ", x)