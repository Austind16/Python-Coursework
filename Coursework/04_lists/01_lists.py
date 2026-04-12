# lists (mutable) (Ordered)
a = ["Batman", "Spiderman", "Ironman", "Thor", 12, 12.8] # list
print(type(a))
print(a)
print(a[3])
a[3] = "Wonder woman"
print(a[3])
print(len(a)) # Length of the string
a.append("Wonder woman") # Adds element to the end of the string
print(a)
print(f"Wonder women count in list = {a.count("Wonder woman")}") # Prints the count of times the element is in the string
a.insert(2,True) # Add element to specific index
print(a)
print(f"First index of Wonder woman = {a.index("Wonder woman")}") # Gives first index of the element
a.remove(True) # Removes the element from the list
print(a)
a.reverse() # Reverses the list
print(a)
a.clear() # Clears the list
print(a)