# Python program to find whether entered number is palindrome or not
a = int(input("Enter number to check: "))
b = a
num = 0
while a > 0:
    digit = a%10
    num = (num*10) + digit
    a //= 10

if b == num:
    print("Entered number is a palindrome number")
else:
    print("Entered number is not a palindrome number")