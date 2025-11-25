# Work with lists

lst = [1,2,3,4,5]

lst.insert(5, 10)
lst.insert(6, 20)
print(f"List after adding 10 and 20 {lst}")
lst.remove(10)
print(f"List after removing 10 {lst}")

# Calculate sum
lst1 = [1,2,3,4,5]
print(f"Sum of list lst1: {sum(lst1)}")

# Double numbers in list
lst2 = [1,2,3,4,5]
lst2_double = []
for item in lst2:
    lst2_double.append(item * 2)

print(f"Double numbers in lst2: {lst2_double}")
