a = int(input("Enter starting range: "))
b = int(input("Enter ending range: "))
for i in range (a,b+1):
    if i>1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)