# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open('./Input/Names/invited_names.txt') as file:
    for name in file.readlines():
        names.append(name)

with open('./Input/Letters/starting_letter.txt') as file:
    content = file.read()
    for i in names:
        stripped_name = i.strip()
        new_content = content.replace('[name]', stripped_name)
        # print(new_content)
        with open(f'./Output/ReadyToSend/{stripped_name}.txt', mode='w') as file:
            file.write(new_content)
