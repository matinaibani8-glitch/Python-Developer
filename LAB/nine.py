# Practical Example 6: Write a Python program to check if a number is prime using if_else.  

# Python Program: Check Prime Number

num = int(input("Enter a number: "))

# Prime numbers must be greater than 1
if num > 1:
    # Check if the number has any divisors
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Print result
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

else:
    print(num, "is not a prime number.")


# How It Works

# First check:

#if num > 1:


