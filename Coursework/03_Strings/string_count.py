# Python program to count characters in a given string (excluding spaces)
# This program helps you learn how to loop through a string and count characters.

# Take input from the user
str = input("Enter string to check: ")

# Find the length of the string
l = len(str)

# Initialize a counter variable
count = 0

# Loop through each character in the string
for i in range(l):
    # If the character is a space, skip it
    if str[i] == " ":
        continue
    else:
        # If not a space, increase the count
        count += 1

# Print the result
print(f"Number of characters in string is: {count}")