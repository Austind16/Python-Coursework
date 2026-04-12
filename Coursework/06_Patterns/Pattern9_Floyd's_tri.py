# Floyd's Triangle
size = int(input("Enter the size of Floyd's triangle: "))
a = 1
for i in range(0,size + 1):
    for j in range(i):
        print(a, end = " ")
        a = a+1
    print()