# Write a python program to create one function to find maximum of three numbers
def maximum(a, b, c):
    if a>b and b>c:
        print(a ,"is the greatest number")
    elif b>c:
        print(b ,"is the greatest number")
    else:
        print(c ,"is the greatest number")

maximum(12,10,5) # Calling function with arguments