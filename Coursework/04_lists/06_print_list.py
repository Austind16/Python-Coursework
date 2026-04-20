
# Printing list values using for loops

# Create a list with different elements
a = ["Batman", "Thor", "Ironman", "Wanda", 12, 12.5, False]

# Find the length of the list
l = len(a)

# Print each element using its index (traditional for loop)
for i in range(l):
    print(a[i], end = " ")

print()  # Print a newline

# Print each element directly (for-each loop)
for i in a:
    print(i)