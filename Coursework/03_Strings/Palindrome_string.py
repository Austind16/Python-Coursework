# Python program to check if given string is palindrome or not
s = input("Enter string to check: ")
s = s.lower()

s1 = (s[-1::-1])
print(f"Reversed string is: {s1}")

if s1 == s:
    print("Entered string is palindrome")
else:
    print("Entered string is not palindrome")