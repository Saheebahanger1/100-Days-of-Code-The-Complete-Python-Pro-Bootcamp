# List Comprehension.

numbers = [1, 2, 3]
"""[new_item for item in list]"""
new_list = [n * 2 for n in numbers]
print(new_list)

# Range List Comprehension.
range_list = [num * 2 for num in range(1,5)]
print(range_list)

# Conditional List Comprehension
names = ['Alex', 'Saheeb', 'Beth', 'Maxy', 'Synx']
short_names = [name for name in names if len(name) <= 4]
print(short_names)
long_names = [name.upper() for name in names if len(name) < 5 ]
print(long_names)


# Dictionary Comprehension.
# new_dict = {new_key:new_value for item in dict.items()}

# Conditional Dictionary Comprehension.
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
names = ['Alex', 'Saheeb', 'Beth', 'Maxy', 'Synx']
students_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

student_dict = {
    "student": ["Saheeb", "Khalid", "Uzair"],
    "score": [98, 55, 67]
}
# Looping through Dictionaries:
for(key,value) in student_dict.items():
    print(value)

import pandas as pd 

student_dataframe = pd.DataFrame(student_dict)
print(student_dataframe)

# Loop through rows of a Dataframe:
for(index, row) in student_dataframe.iterrows():
    print(row.score)


# NATO ALPHABET PROJECT.
import pandas as pd 
data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)