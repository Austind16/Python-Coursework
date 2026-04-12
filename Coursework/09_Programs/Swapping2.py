# Python program to swap two numbers without using 3rd variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before Swapping: a={a} and b={b}")

#Swapping using only two variable logic
a = a+b 
b = a-b
a = a-b

print(f"After Swapping: a={a} and b={b}")