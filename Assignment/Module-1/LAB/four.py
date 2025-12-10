# • Practical Example 1: How does the Python code structure work?

"""
This program calculates the area of a rectangle.
It demonstrates how a Python program is structured properly.
"""

# 1. Import statements (if needed)
import math

# 2. Global variables / constants
PI = 3.14

# 3. Function definitions
def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width


def display_result(area):
    """Print the final result."""
    print(f"The area of the rectangle is: {area}")


# 4. Main program logic
def main():
    """Main function of the program."""
    
    # Input from the user
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    # Processing
    area = calculate_area(length, width)

    # Output
    display_result(area)


# 5. Program execution starts here
if __name__ == "__main__":
    main()
