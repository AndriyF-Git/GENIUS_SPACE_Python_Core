#Multiply sheet
number = int(input("Enter a number: "))

for iterator in range(1, 10):
    print(f"Result multiplying {number} by {iterator} is {number * iterator}")

# Sum of numbers
input_num = list(input("Enter a set of numbers: "))
sum_of_numbers = 0
lst_num = 0
for num in input_num:
    try:
        lst_num = int(num)
        print(lst_num)
    except ValueError:
        print(f"Error, {num} it`s not a number")

    if num.isdigit():
        sum_of_numbers = lst_num + sum_of_numbers

print(f"Sum of numbers: {sum_of_numbers}")


number = int(input("Enter a number: "))
fact = 1
for i in range(1, number + 1):
    print(i)
    fact = fact * i

print(f"Factorial of {number} is {fact}.")

# even numbers
for i in range(1, 51):
    if i % 2 == 0:
        print(i)


#simple numbers
input1 = int(input("Enter a number1: "))
input2 = int(input("Enter a number2: "))

is_simple = False
for i in range(input1, input2):
    if i % 2 != 0:
        #print(f"i on first cycle {i}")
        if i == 1 or i == 3:
            print(f"{i} is simple")
        for each in range(i - 2, 2, -2):
            #print(f"each: {each}")
            if i % each != 0:
                if each == 3:
                    print(f"{i} is simple")
                continue
            else:
                break


