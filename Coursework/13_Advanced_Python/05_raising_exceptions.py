a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if b ==0:
    raise ZeroDivisionError("You cannot divide number by zero")

else:
    print(f"The Quotient of the two numbers are: {a/b}")