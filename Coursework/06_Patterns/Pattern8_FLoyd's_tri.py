# Floyd's Triangle
size = int(input("Enter the starting number: "))
for i in range(0,size+1):
    for j in range(i):
        print(size, end = " ")
        size = size + 1
    print()