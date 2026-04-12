# Python program to find factorial of given no.
a = int(input("Enter number to find factorial of: "))

for i in range(1,a):
    a *= i

print(f"{a} is the factorial of the number")