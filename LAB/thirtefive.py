#• Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce() and lambda to find the product
product = reduce(lambda x, y: x * y, numbers)

print("List of numbers:", numbers)
print("Product of numbers:", product)

