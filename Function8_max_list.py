# Wap to find maximum value from given list
n = int(input("Enter number of entries you want: "))
a = []
for i in range (0,n):
    num = int(input(f"Enter number{i+1}: "))
    a.append(num)

def max_of_list(a):
    max = 0
    for i in a:
        if max<i:
            max = i
    return max

print("List is: ", a)
result = max_of_list(a)
print("Max number is: ", result)