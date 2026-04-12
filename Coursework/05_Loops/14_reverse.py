# Python program to reverse a user entered number
a = int(input("Enter number to reverse: "))

num = 0
while a > 0:
    digit = a%10
    num = (num*10) + digit
    a //= 10

print(f"{num} is the reversed number")