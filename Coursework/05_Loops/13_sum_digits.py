# Python program to find sum of digits of a number
a = int(input("Enter number to perform operation on: "))

sum = 0
while a > 0:
    num = a%10
    sum += num
    a //= 10

print(f"{sum} is the sum of the digits of the number")