#• Write a Python program to apply the map() function to square a list of numbers.

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map() and lambda to square each number
squared_numbers = list(map(lambda x: x**2, numbers))

# Print the result
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)

