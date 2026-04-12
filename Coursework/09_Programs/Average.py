# Python program to input marks of three subjects of a student, calculate and print average of students marks
name = input("Enter student name: ")
a = int(input("Enter student marks 1: "))
b = int(input("Enter student marks 2: "))
c = int(input("Enter student marks 3: "))

avg = (a+b+c)/3

print(f"Average of {name} marks are: {avg}")