try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print("Please enter a number not anything else")
    
except Exception as e:
    print(e) 

print("Thank You")