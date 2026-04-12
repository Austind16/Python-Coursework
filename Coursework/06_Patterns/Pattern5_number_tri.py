# Numbered pattern(Right triangle)
# row = i
# column = j
size = int(input("Enter size of pattern: "))
for i in range (0, size):
    for i in range (0,i+1):
        print(i + 1, end = " ")
    print()