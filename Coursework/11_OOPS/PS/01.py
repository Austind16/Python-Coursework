class Employee:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

Mark = Employee("Mark", 130000, 392110)
print(Mark.company, Mark.name, Mark.salary, Mark.pin)
Naveen = Employee("Naveen", 150000, 456230)
print(Naveen.company, Naveen.name, Naveen.salary, Naveen.pin)