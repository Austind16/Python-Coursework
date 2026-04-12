class Employee:
    language = "Py" #  This is a class attribute
    salary = 120000

Mark = Employee()
Mark.language = "JavaScript"
print(Mark.language, Mark.salary)

# Instance attribute is given preference over class attribute