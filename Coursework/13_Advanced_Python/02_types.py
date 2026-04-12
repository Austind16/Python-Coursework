from typing import List, Union, Tuple, Dict

numbers : List[int] = [1, 2, 3]
person : Tuple[str, int] = ["Alice", 30]
scores : Dict[str, int] = {"Alice": 90, "Padma": 45}
Identifier : Union[str, int] = "ID123"

n : int = 5 # Integer type declared
str : str = "Python" # String type declared
f : float = 42.069 # Float type declared
b : bool = True # Boolean type declared

print(type(n))
print(type(str))
print(type(f))
print(type(b))

def sum(a: int, b: int) -> int:
    return a+b

sum(5,4)