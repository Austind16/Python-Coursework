class Employee:
    language = "Py" #  This is a class attribute
    salary = 120000

    def __init__(self, name, language, salary): # Dunder method which is called by itself
        self.name = name
        self.language = language
        self.salary = salary

        print("I am calling an object")

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

Mark = Employee("Mark", "JavaScript", 130000)
print(Mark.name, Mark.language, Mark.salary)