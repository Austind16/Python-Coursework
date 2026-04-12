# Python program to check if user entered character is a vowel or not
a = input("Enter character to check: ")
a = a.lower() # Changing character to lower case to avoid errors of lower and upper case
if a == 'a' or a == 'e' or a =='i' or a == 'o' or a == 'u':
    # If loop to check if entered character is a vowel or not
    print("Entered character is a vowel")
else:
    print("Entered character is a consonant")