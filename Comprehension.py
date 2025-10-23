# List Comprehension in Python 

numbers = [1, 2, 3]

new_list = [no + 1 for no in numbers]

print(new_list) 
 
name = "Aadarsh"

new_list = [letter for letter in name] 

print(new_list)

range_list = [ num * 2 for num in range(1, 11) if num % 2 == 0]

print(range_list)

name_list = ["Alex", "Beth", "Carolina", "Dave", "Elanor", "Freddie", "Anie"]

short_name = [name for name in name_list if len(name) <= 4]

print(short_name)

long_name = [name for name in name_list if len(name) > 4]

print(long_name)

# Day-26-1-Exercise

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [no ** 2 for no in numbers]

print(squared_numbers)


# Day-26-2-Exercise

result = [no for no in numbers if no % 2 == 0]

print(result)


# Day-26-3-Exercise

list1 = []
list2 = []

with open("26thDay\File1.txt", "r") as file1 :
    raw_list = file1.readlines()
    list1 = [int(no.strip()) for no in raw_list]
 
with open("26thDay\File2.txt", "r") as file2 :
    raw_list = file2.readlines()
    list2 = [int(no.strip()) for no in raw_list]
        
common_no = [no for no in list1 if no in list2] 

print(common_no) 

# Dictionary Comprehension in Python

 