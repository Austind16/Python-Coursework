# Hollow square
# nested loop 
# row = i
# column = j
size = int(input("Enter size of the square: "))
for i in range(0, size):
    for j in range(0, size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()