# Python program to print 1 to 10 but if 6 comes loop gets terminated

i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break # Terminates the loop

i = 0
while i <= 9:
    i += 1
    if i == 6:
        continue # skips one condition
    print(i)