# Write a python program to take user input and insert values into list pf friends
f = int(input("Enter number of friends: "))
a = []

for i in range (0,f):
    name = input(f"Enter name of friend {i+1}:")
    a.append(name)
print(f"Your friends are: {a}")