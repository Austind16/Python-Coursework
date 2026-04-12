class Employee:
    company = "ITC"
    name = "Mark"
    salary = 150000
    language = "Python"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder:
    language = "JavaScript"
    def printLanguages(self):
        print(f"Out of all languages here is your language: {self.language}")

class Programmer(Coder, Employee):
    company = "ITC Infotech"
    name = "Naveen"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

b = Programmer()
print(b.company, b.name, b.language)
b.show()
b.printLanguages()
b.showLanguage()