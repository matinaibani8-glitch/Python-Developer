# • Write a generator function that generates the first 10 even numbers.

# Python Generator for First 10 Even Numbers
def generate_even_numbers():
    num = 2
    count = 0
    while count < 10:
        yield num
        num += 2
        count += 1

# Using the generator
for n in generate_even_numbers():
    print(n)