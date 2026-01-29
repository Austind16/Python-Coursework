def odd_even(no):
    if(no%2 == 0):
        return 1
    else:
        return 0 
n = int(input("Enter number: "))
result = odd_even(n)
print("Result is: ",result)

if result == 0:
    print("Odd number")
else:
    print("Even number")