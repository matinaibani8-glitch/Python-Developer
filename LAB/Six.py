# • Practical Example 3: How to take user input using the input() function.

name = input("Enter your name: ")
print("Hello,", name)

#Integer Example
age = int(input("Enter your age: "))
print("Your age is:", age)

#Float Example
price = float(input("Enter product price: "))
print("Price is:", price)

#Taking multiple inputs in one line

a, b = input("Enter two numbers separated by space: ").split()
print("a =", a)
print("b =", b)

a, b = map(int, input("Enter two numbers: ").split())
print(a + b)

# Mini Program Using User Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old!")
