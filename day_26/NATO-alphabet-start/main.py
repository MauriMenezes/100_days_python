import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_phonetic)
new_dict = {row.letter: row.code for (index, row) in nato_phonetic.iterrows()}
print(new_dict)


is_ok = True
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# while is_ok:
#     try:
#         user_input = input('write a word : ').upper()
#         output_list = [new_dict[i] for i in user_input]
#         print(output_list)
#         is_ok = False

#     except KeyError:
#         print('Sorry, only letters in the alphabet please.')


def generate_phonetic():
    word = input('write a word : ').upper()
    try:
        output_list = [new_dict[i] for i in word]
        print(output_list)
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()

# user_input = input('write a word : ').upper()
###
# for each 1° letter in a word

# list_strings = user_input.split()
# # print(list_strings)
# list_codes = []
# for i in list_strings:
#     for (key, value) in new_dict.items():
#         if i[0] == key:
#             list_codes.append(value)
# print(list_codes)

##############
# for each letter in a word

# output_list = [new_dict[i] for i in user_input]
# print(output_list)
