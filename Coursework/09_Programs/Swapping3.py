# Using python's attribute to swap two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"Before swapping: a={a} and b={b}")

a,b = b,a # using Python attribute to swap

print(f"After swapping: a={a} and b={b}")