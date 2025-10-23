# NATO Alphabet Project in Python

import pandas

data = pandas.read_csv("26thDay\Alphabets.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter a word: ").upper()

nato_list = [data_dict[letter] for letter in name if letter in data_dict]
    
print(nato_list)    