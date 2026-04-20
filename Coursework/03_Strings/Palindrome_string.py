# Python program to check if a given string is a palindrome
# A palindrome is a word that reads the same forwards and backwards (like 'madam' or 'racecar').

# Take input from the user
s = input("Enter string to check: ")

# Convert the string to lowercase to ignore case differences
s = s.lower()

# Reverse the string using slicing
# s[-1::-1] means start from the last character and go backwards
s1 = s[-1::-1]

# Print the reversed string
print(f"Reversed string is: {s1}")

# Compare the original and reversed strings
if s1 == s:
    print("Entered string is palindrome")
else:
    print("Entered string is not palindrome")