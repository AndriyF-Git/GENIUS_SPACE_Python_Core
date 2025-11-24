num_str = 125
num_str = str(num_str)
print(f"Type of variable num_str is {type(num_str).__name__}")

message = 'Hi, my name is Python'
print(f"Modified message is {message.replace('y', '0').replace('i', '1')}")


split_test = 'This is a split test'
print(f'Split message  {split_test.split()}')

string_join ='This is a string join test'
print(f'string_join length {len(string_join)}')

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(f'list_append  {list_append}')
print(f'list_append length is {len(list_append)}')

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(f'list_extend  {list_extend}')
print(f'list_extend element 6 have index {list_extend.index(6)}')

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(f'dict_test value of key car is {dict_test.get("car")} and value of key where is {dict_test.get("where")}')
print(f"all keys in dict_test is {dict_test.keys()}")
print(f"all items in dict_test is {dict_test.items()}")
