class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

o = Employee()
print(o.a) # Prints 1
# print(o.b) # Shows error as there is no b attribut in employee

o = Programmer()
print(o.a, o.b)
# print(o.c) # Shows error as there is no c attribute in programmer

o = Manager()
print(o.a, o.b, o.c)