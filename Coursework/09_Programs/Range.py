# Write a function to check wether a given number falls in given range
a = int(input("Enter number between 10 and 20: "))
def fun (a):
    if a>10 and a<20:
        print("Entered number is within the range")
    else:
        print("Entered number is not in range")

fun(a)