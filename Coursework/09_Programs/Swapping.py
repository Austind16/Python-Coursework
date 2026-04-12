# Write a program to swap two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swapping: a={a} and b={b}")

temp = a # storing a in a temporary variable
a = b
b = temp # taking value from temporary variable to b

print(f"After swapping: a={a} and b={b}")