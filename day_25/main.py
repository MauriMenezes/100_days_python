
# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)
# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv('weather_data.csv')
# # print(data)
# data_dict = data.to_dict()
# # print(data_dict)

# # Get Data in Colum

temp_list = data['temp']
print(temp_list)

# avarage = round(sum(temp_list) / len(temp_list), 2)
# print(avarage)

# print(data['temp'].max())

# Get Data in Row

print(data[data['day'] == 'Monday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
monday_temp = monday.temp
monday_temp_F = monday_temp * 9/5 + 32
print(int(monday_temp_F))

# creating a dataFrame form scratch

# data_dict = {
#     "students": ['Amy', 'Carolin', 'Maurilio'],
#     "scores": [30, 60, 90]
# }

# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv('new_data.csv')


# data = pandas.read_csv('squirrel_data.csv')
# # print(data.keys())

# gray_squirrel_count = len(data[data['Primary Fur Color'] == "Gray"])
# black_squirrel_count = len(data[data['Primary Fur Color'] == "Black"])
# # red_squirrel_count = len(data[data['Primary Fur Color'] == "Red"])
# cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == "Cinnamon"])


# data_dict = {

#     "Fur Color": ['gray', 'black', 'red'],
#     "count": [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
# }
# analise = pandas.DataFrame(data_dict)
# analise.to_csv('analise_squirrels.csv')
