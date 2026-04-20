
# Tuples in Python (immutable and ordered)
# A tuple is like a list, but you cannot change its values after creation.

# Create a tuple with different elements
a = ("America", "India", "China", 12, 12.46, True)

# Print the type of 'a' (should be <class 'tuple'>)
print(type(a))

# Print the whole tuple
print(a)

# Print the element at index 3 (fourth element)
print(a[3])

# Print the length of the tuple
print(len(a))

# Count how many times 'America' appears in the tuple
print(a.count("America"))

# Find the index of 'China' in the tuple
print(a.index("China"))