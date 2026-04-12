# Python program to create a simple calculator where two inputs given by the user and which operation wants to perform is given by the user acc. to that sign
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = input("Enter sign of operation you want to perform: ")

# if, elif and else statements check the condition and perform the respective operation
if c == '+':
    print("Sum of numbers are: ", a+b)
elif c == '-':
    print("Difference of numbers are: ", a-b)
elif c == '*':
    print("Product of numbers are: ", a*b)
elif c == '/':
    print("Quotient of numbers are: ", a/b)
elif c == '%':
    print("Modulus of numbers are: ", a%b)
else:
    print("Unidentified entry")