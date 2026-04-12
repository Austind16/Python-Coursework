class Animals:
    @staticmethod
    def statement():
        print("Bhow Bhow !!")

class Pets(Animals):
    pass

class Dog(Pets):
    @classmethod
    def bark(cls):
        super().statement()

d = Dog()

d.bark()