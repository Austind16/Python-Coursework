
# Sets in Python (mutable, unordered, no duplicates)
# A set is a collection of unique values. The order is not guaranteed.

# Create two sets with different elements
set1 = {"Apple", "Banana", "Cherry", 12, 12.5, True}
set2 = {"Guava", "Banana"}

# Print the type of set1 (should be <class 'set'>)
print(type(set1))

# Print all elements in set1
print(set1)

# Print the number of elements in set1
print(len(set1))

# Add a new element to set1
set1.add("ABC")
print(set1)

# Remove the element 'ABC' from set1
set1.remove("ABC")
print(set1)

# Remove all elements from set1
set1.clear()
print(set1)