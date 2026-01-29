# WAP to create a function to find minimum value in a list
n = int(input("Enter number of entries you want: "))
a = []
for i in range (0,n):
    num = int(input(f"Enter number{i+1}: "))
    a.append(num)

def min_of_list(a):
    min = a[0]
    for i in a:
        if min>i:
            min = i
    return min

print("List is: ", a)
result = min_of_list(a)
print("Min number is: ", result)