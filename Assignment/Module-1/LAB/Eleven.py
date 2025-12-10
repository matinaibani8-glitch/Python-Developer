# Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.

# Python Program: Blood Donation Eligibility

age = int(input("Enter your age: "))
weight = int(input("Enter your weight (in kg): "))

if age >= 18:
    # Nested if for weight
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible because your weight is less than 50 kg.")
else:
    print("You are not eligible because your age is below 18.")
