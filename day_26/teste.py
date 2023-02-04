# numbers = [1, 2, 3]

# new_numbers = [i+1 for i in numbers]
# print(new_numbers)

# nome = 'maurilio'

# letter_list = [i.replace('a', "c") for i in nome]

# print(letter_list)

# sequence = [i * 2 for i in range(1, 6) if i > 2]
# print(sequence)

import pandas
import random
names = ['maurilio', 'miriam', 'mauricio', 'mauricio']

# new_names = [i.upper() for i in names]

# print(new_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# # squared_numbers = [i ** 2 for i in numbers]
# # print(squared_numbers)
# even_num = [i for i in numbers if i % 2 == 0]
# print(even_num)

# with open('file1.txt') as file:
#     lista1 = [int(i) for i in file]

# with open('file2.txt') as file:
#     lista2 = [int(i) for i in file]

# result = [i for i in lista1 if i in lista2]
# print(result)

# dict comprehension


# students_scores = {i: random.randint(20, 100) for i in names}
# print(students_scores)

# passed_students = {name: score for name,
#                    score in students_scores.items() if score > 60}
# print(passed_students)

# sentence = 'This is a sentence'

# # new_sentence = sentence.split()
# # print(new_sentence)


# def convert(lista):
#     return [i for i in lista.split()]


# converted_list = convert(sentence)
# new_dict = {word: len(word) for word in converted_list}
# print(new_dict)


# wheater_c = {
#     'week': ['day', 'temp'],
#     'Monday': 12,
#     'Tuesday': 14,
#     'wednesday': 15,
#     'Thursday': 21,
#     'Friday': 14,
#     'Saturday': 22,
#     'Sunday': 25,
# }

# wheater_f = {day: ((temp * 9/5) + 32) for day, temp in wheater_c.items()}
# print(wheater_f)

student_dict = {
    'names': ['maurilio', 'miriam'],
    'notas': [3, 5]
}

new_data = pandas.DataFrame(student_dict)
# print(new_data)
# new_data.to_csv('new_dataa.csv')

# loop through a data frame

# for (key, value) in new_data.items():
#     print(value)

# loop through rows

for i, row in new_data.iterrows():
    print(row)
