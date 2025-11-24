lst = [1, 2, 3, 4, 5, 39]
dct = {
    "name": "John",
    "age": 39,
    "surname": "Marston", }

boolean = False
number = 3
name = "Tom"
tpl = ("n", "a", "g")

result = dct.get("age") not in lst == boolean
print(f"Condition 1 is", result)

result = number in lst and tpl[1] in dct.get("surname")
print(f"Condition 2 is",result)

check = None

print(f"Condition 3 is", dct["name"] == name or dct["age"] in lst is not None)