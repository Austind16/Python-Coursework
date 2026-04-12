class Employee:
    language = "Py" #  This is a class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greeting():
        print("Good morning")

Mark = Employee()
Mark.greeting()
Mark.getInfo()