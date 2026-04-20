
# Program to take user input and store friend names in a list

# Ask the user how many friends they want to enter
f = int(input("Enter number of friends: "))

# Create an empty list to store friend names
a = []

# Loop to take input for each friend
for i in range(f):
    # Ask for the friend's name
    name = input(f"Enter name of friend {i+1}:")
    # Add the name to the list
    a.append(name)

# Print the final list of friends
print(f"Your friends are: {a}")