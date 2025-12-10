'''Write a Python program that demonstrates the correct use of indentation, comments, and
variables following PEP 8 guidelines.'''


"""
This program calculates the total cost of items after applying a discount.
It demonstrates proper indentation, comments, and variable naming conventions.
"""

# Constant (written in ALL_CAPS)
DISCOUNT_RATE = 0.10  # 10% discount


def calculate_discounted_price(original_price):
    """
    Calculate the price after applying discount.
    
    Parameters:
        original_price (float): The initial price of the item.
    
    Returns:
        float: Price after discount.
    """
    discounted_amount = original_price * DISCOUNT_RATE
    final_price = original_price - discounted_amount
    return final_price


def main():
    """Main function to run the program."""
    
    # Input from the user
    item_price = float(input("Enter the item price: "))
    
    # Calculate final price
    final_price = calculate_discounted_price(item_price)
    
    # Display result
    print(f"Final price after discount: ₹{final_price:.2f}")


# Program execution starts here
if __name__ == "__main__":
    main()