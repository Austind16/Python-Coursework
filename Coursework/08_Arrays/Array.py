import array as arr

# f = float - 4 bytes
# l = long - 4 bytes
# u = char - 2 bytes

a = arr.array('i', [1, 2, 3, 4, 5, 6]) # i = integer
print(a)
print(a[0])

for i in a:
    print(i, end = " ")
print()

b = arr.array('d', [2.5, 3.2, 3.3]) # d = double(Float - 8bytes)
print(b)
print(b[1])

for i in b:
    print(i, end = " ")
print()

print(a[2:5])
print(a[0:5:2])

sum = 0
for i in a:
    sum += i
print(f"Sum of array elements a are: {sum}")

sum = 0
for i in b:
    sum += i
print(f"Sum of array elements b are: {sum}")

a.append(8)

for i in a:
    print(i, end = " ")
print()

a.remove(4)
for i in a:
    print(i, end = " ")
print()

a.insert(3,4)
for i in a:
    print(i, end = " ")
print()