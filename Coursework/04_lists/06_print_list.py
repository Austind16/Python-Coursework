# Printing list values using for loop
a = ["Batman", "Thor", "Ironman", "Wanda", 12, 12.5, False]
l = len(a)
for i in range (l):
    print(a[i], end = " ")

for i in a:
    print(i)