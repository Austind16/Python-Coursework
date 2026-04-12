# Python program to search a number in an array
import array as arr

a = arr.array('i', [])

size = int(input("Enter size of the array: "))

for i in range(size):
    num = int(input(f"Enter number {i+1}: "))
    a.append(num)

print("Your array is: ")
for i in a:
    print(i, end = " ")
print()

find = int(input("Enter number to search: "))

for i in a:
    if i == find:
        print("Number found at: {a.index(find)}")
        break
else:
    print("-1")