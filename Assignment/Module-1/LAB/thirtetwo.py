# Write a Python program that manipulates and prints strings using various string methods.

text = "   python programming is fun!   "

# 1. Convert to uppercase
print("Uppercase:", text.upper())

# 2. Convert to lowercase
print("Lowercase:", text.lower())

# 3. Capitalize first letter
print("Capitalized:", text.capitalize())

# 4. Title case (first letter of each word capitalized)
print("Title Case:", text.title())

# 5. Remove leading and trailing spaces
print("Stripped:", text.strip())

# 6. Replace a word
print("Replace 'python' with 'Python':", text.replace("python", "Python"))

# 7. Split string into a list of words
words = text.strip().split()
print("Split into words:", words)

# 8. Join list of words into a single string
joined_text = "-".join(words)
print("Joined with '-':", joined_text)

# 9. Check if string starts or ends with a specific substring
print("Starts with 'python':", text.strip().startswith)
