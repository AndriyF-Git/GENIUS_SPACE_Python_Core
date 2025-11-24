text = "string"
number = 1
number_float = 1.1
boolean = True
lst = [1, 2, 3]
tpl = (1, 2, 3)
dct = {
    "Name": "John",
    "Age": 39,
    "Surname": "Marston", }

print(f"Type of text variable", type(text).__name__)
print(f"Type of number variable", type(number).__name__)
print(f"Type of number_float variable", type(number_float).__name__)
print(f"Type of list variable", type(lst).__name__)
print(f"Type of tuple variable", type(tpl).__name__)
print(f"Type of dict variable", type(dct).__name__)
print(f"Type of None", type(None).__name__)

class Person:
    pass

a = Person()
print(f"Type of a variable",type(a).__name__)
