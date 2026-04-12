# Python program to count characters in given string
str = input("Enter string to check: ")

l = len(str)

count = 0
for i in range (l):
    if str[i] == " ":
        continue
    else:
        count += 1
        
print(f"Number of characters in string is: {count}")