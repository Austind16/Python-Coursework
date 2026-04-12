# Python program to check wheter entered number is armstrong number or not
a = int(input("Enter number to check: "))
b = a
l = len(str(a))

sum = 0
while a > 0:
    digit = a%10
    sum = sum + (digit**l)
    a //= 10

if sum == b:
    print("Entered number is armstrong number")
else:
    print("Entered number is not armstrong number")