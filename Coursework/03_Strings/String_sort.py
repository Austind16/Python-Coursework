# Python program where one string is given, arrange string characters such that lower case letters should come first
a = input("Enter the string: ")
l = len(a)
s = ""
s1 = ""

for i in range (l):
    if a[i].islower():
        s += a[i]
    else:
        s1 += a[i]

string = s + s1
print(f"The final string is: {string}")