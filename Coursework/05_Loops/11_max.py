# Python program to find greatest of three number entered by the user
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b and a > c:
    print(f"{a} is the greatest number")
elif b > a and b > c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")