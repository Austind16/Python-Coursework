# Sets (Mutable) (Unordered) (No duplicate values)
set1 = {"Apple", "Banana", "Cherry", 12, 12.5, True}
set2 = {"Guava", "Banana"}
print(type(set1))
print(set1)
print(len(set1))
set1.add("ABC")
print(set1)
set1.remove("ABC")
print(set1)
set1.clear()
print(set1)