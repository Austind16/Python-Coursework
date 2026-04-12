# Python program where an array is given, take 1 input from user and search that value in the array, if value found in array it returns its index else returns -1
import array as arr

a = arr.array('i', [10, 15, 5, 7, 12])
l = len(a)

user = int(input("Enter number to search: "))

for i in range(l):
    if a[i] == user:
      print(f"Element found at : {i}")
      break
else:
    print("-1")