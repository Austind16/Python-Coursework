
# Python program to arrange string characters so that lowercase letters come first
# This helps you practice string manipulation and character checking.

# Take input from the user
a = input("Enter the string: ")

# Find the length of the string
l = len(a)

# Create two empty strings to store lowercase and other characters
s = ""
s1 = ""

# Loop through each character in the string
for i in range(l):
    # If the character is lowercase, add to s
    if a[i].islower():
        s += a[i]
    else:
        # If not lowercase, add to s1
        s1 += a[i]

# Combine lowercase and other characters
string = s + s1

# Print the final string
print(f"The final string is: {string}")