import smtplib
import datetime as dt
import random
import pandas

my_email = 'maumenezes20@gmail.com'
password = 'tsqxzczibnmmvpgr'

# SENDING QOUTES
# birth = dt.datetime(year=2002, month=6, day=7)
# print(birth)
# # challenge

# with open('quotes.txt') as file:

#     quotes = [i for i in file.readlines()]
#     choice = random.choice(quotes)
#     print(choice)


# now = dt.datetime.now()
# today = now.weekday()
# if today == 2:
#     print('wendsday')
#     with smtplib.SMTP('smtp.gmail.com') as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs='mau_menezes@yahoo.com', msg=f'Subject: Quotes \n\n {choice}')

##################### HAPPY BIRTHDAY PROJECT ######################


data = pandas.read_csv('birthdays.csv')

data_dict = {(data_row['month'], data_row['day']): [data_row['name'], data_row['email']]
             for (_, data_row) in data.iterrows()}

now = dt.datetime.now()
today = (now.month, now.day)

if today in data_dict:
    person = data_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        content = letter_file.read()
        new_content = content.replace("[NAME]", person[0])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f'{person[1]}', msg=f'Subject: HAPPY BIRTHDAY \n\n {new_content}')
