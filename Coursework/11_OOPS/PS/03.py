class Demo:
    a = 4

o = Demo()
print(o.a) # Prints class attribute as instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints instance attribute as it is present
print(Demo.a) # Directly prints class attribute as it remains unchanged