# • Practical Example 5: Write a Python program to find greater and less than a number using
# if_else.

# Program 1: Compare user input with a fixed number

num = int(input("Enter a number: "))

if num > 10:
    print("The number is greater than 10.")
elif num < 10:
    print("The number is less than 10.")
else:
    print("The number is exactly 10.")

# Program 2: Compare two user inputs

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is less than", b)
else:
    print("Both numbers are equal.")

# Output Example:

# If user enters 12 and 9:

#12 is greater than 9
