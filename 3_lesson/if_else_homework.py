# Password check
password = "password123"
input_password = input("Enter password: ")

if input_password == password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

# Weekdays
weekdays_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

input_num_of_day = int(input("Enter a number of weekday: "))
if input_num_of_day in range(1, 7):
    real_num_of_weekday = input_num_of_day - 1
    print(f"Weekday by number is {weekdays_list[real_num_of_weekday]}")
else:
    print("Invalid input")
