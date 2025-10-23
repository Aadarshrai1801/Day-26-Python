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

import random 

name_list = ["Alex", "Beth", "Carolina", "Dave", "Elanor", "Freddie", "Anie"]

student_scores = {name: random.randint(1, 101) for name in name_list}

print(student_scores)

passed_student = {name for (name, score) in student_scores.items() if score >= 60}

print(passed_student)


# Day-26-4-Exercise

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {letter: len(letter) for letter in sentence.split()}

print(result)


# Day-26-5-Exercise

weather_c = {
    "Monday": 12, 
    "Tuesday": 14,
    "Wednesday" : 15,
    "Thursday": 14, 
    "Friday": 21,
    "Saturday": 22, 
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

print(weather_f)


# Iteration in Pandas DataFrame

import pandas

student_dict = {
    "Student" : ["Aadarsh", "Rohan", "Ritesh", "Aniket"],
    "Score" : [100, 34, 100, 30]
}

data = pandas.DataFrame(student_dict) 

print(data)

# Looping through Pandas DataFrame 

for (index, rows) in data.iterrows() :
    if rows.Score == 100 :
        print(rows.Student)