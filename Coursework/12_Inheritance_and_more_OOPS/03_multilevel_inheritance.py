class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints 1
# print(o.b) # Shows error as there is no b attribut in employee

o = Programmer()
print(o.a, o.b)
# print(o.c) # Shows error as there is no c attribute in programmer

o = Manager()
print(o.a, o.b, o.c)