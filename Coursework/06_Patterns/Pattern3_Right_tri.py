# Normal right triangle
# Nested looping
# i for row
# j for column
for i in range (0,5):
    for j in range (0,5):
        print(end = " ")
    for j in range (0,i+1):
        print("*", end = " ")
    print()