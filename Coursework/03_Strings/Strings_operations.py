
# Examples of basic string operations in Python

# Assign a string to a variable
x = "Hello World"

# Print the length of the string
print("Length: ", len(x)) # len(x) gives the number of characters

# Print the first character (index 0)
print(x[0])

# Print characters from index 2 to 4 (index 5 is not included)
print(x[2:5])

# Convert the string to uppercase
print(x.upper())

# Convert the string to lowercase
print(x.lower())

# Replace 'H' with 'J' in the string
print(x.replace("H", "J"))

# Reverse the string using slicing
print(x[-1::-1])

# Print the last 3 characters
print(x[-3:])

# Print every second character from index 0 to 8
print(x[0:9:2])