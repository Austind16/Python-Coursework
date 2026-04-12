# Python program to check whether entered number is prime number or not
a = int(input("Enter number to check: "))

for i in range (2,a):
    if a%i == 0:
        print("Entered number is not prime number: ")
        break
else:
        print("Entered number is prime number: ")