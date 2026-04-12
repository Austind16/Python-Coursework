# Python program to take three subjects marks of one student, if total of marks is greater or equal to 90, print grade A, if marks is greater or equal to 75 then print grade B, if marks is greater or equal to 60 then grade c and if greater or equal to 50 then grade D
name = input("Enter student name: ")

a = int(input("Enter marks of 1st subject: "))
b = int(input("Enter marks of 2nd subject: "))
c = int(input("Enter marks of 3rd subject: "))

# Calculating average marks (percentage)
total = (a+b+c)/3

# Checking grade according to the percentage
if total>=90:
    print(f"{name} got grade A and scored {total}%")
elif total>=80:
    print(f"{name} got grade B and scored {total}%")
elif total>=75:
    print(f"{name} got grade C and scored {total}%")
elif total>=60:
    print(f"{name} got grade D and scored {total}%")
else:
    print(f"{name} failed")