'''Practical Example 3: Write a Python program to find a specific string in the list using a simple
for loop and if condition.'''

# Practical Example 3: Find a Specific String in a List Using for Loop + if

List1 = ['apple', 'banana', 'mango']

search = input("Enter the fruit you want to search: ")

found = False

for item in List1:
    if item == search:
        found = True
        break

if found:
    print(search, "is found in the list.")
else:
    print(search, "is not found in the list.")

