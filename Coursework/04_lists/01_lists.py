
# Lists in Python (mutable and ordered)
# A list can store different types of values and you can change its contents.

# Create a list with different elements
a = ["Batman", "Spiderman", "Ironman", "Thor", 12, 12.8]

# Print the type of 'a' (should be <class 'list'>)
print(type(a))

# Print the whole list
print(a)

# Print the element at index 3 (fourth element)
print(a[3])

# Change the value at index 3
a[3] = "Wonder woman"
print(a[3])

# Print the length of the list
print(len(a))

# Add a new element to the end of the list
a.append("Wonder woman")
print(a)

# Count how many times 'Wonder woman' appears in the list
print(f"Wonder women count in list = {a.count('Wonder woman')}")

# Insert a value (True) at index 2
a.insert(2, True)
print(a)

# Find the first index of 'Wonder woman'
print(f"First index of Wonder woman = {a.index('Wonder woman')}")

# Remove the value True from the list
a.remove(True)
print(a)

# Reverse the order of the list
a.reverse()
print(a)

# Clear all elements from the list
a.clear()
print(a)