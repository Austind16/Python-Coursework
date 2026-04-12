class Employee:
    language = "Py" #  This is a class attribute
    salary = 120000

Mark = Employee()
Mark.name = "Mark" # This is an object attribute
print(Mark.name, Mark.language, Mark.salary)

Naveen = Employee()
Naveen.name = "Naveen" # This is an object attribute
print(Naveen.name, Naveen.language, Naveen.salary)