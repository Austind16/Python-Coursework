# WAP to create a function to sum all numbers in a list taken from the user

num = int(input("How many numbers you want to enter: "))

a = []  # empty list to store numbers

# taking input from the user
for i in range(num):
    n = int(input(f"Enter number {i+1}: "))
    a.append(n)

# function to calculate sum of list elements
def sum_of_list(a):
    total = 0                 # variable to store sum
    for i in range(len(a)):   # loop through the list
        total += a[i]
    print("Sum of the numbers are: ", total)

# function call and printing the result
print("List is: ", a)
sum_of_list(a) 