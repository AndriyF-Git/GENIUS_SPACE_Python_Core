# Work with tuples
tpl = ("яблуко", "банан", "апельсин")
for item in range(len(tpl)):
    print(f"Element {item} in tpl is {tpl[item]}")

# Two tuples in one
tpl1 = (1,2,3,4,5)
tpl2 = (6,7,8,9,10)
tpl3 = tpl1 + tpl2
print(f"United tuple is {tpl3}")