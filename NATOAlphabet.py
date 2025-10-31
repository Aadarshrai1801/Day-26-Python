# NATO Alphabet Project in Python

import pandas

data = pandas.read_csv("26thDay\Alphabets.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def func() :
    name = input("Enter a word: ").upper()

    try :
        nato_list = [data_dict[letter] for letter in name]
    except KeyError :
        print("Sorry, only letters in the alphabet please!")
        func()
    else :
        print(nato_list)
        
func()                    