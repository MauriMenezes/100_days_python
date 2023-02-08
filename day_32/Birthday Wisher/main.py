import smtplib
import datetime as dt
import random

my_email = 'maumenezes20@gmail.com'
password = 'tsqxzczibnmmvpgr'


birth = dt.datetime(year=2002, month=6, day=7)
print(birth)
# challenge

with open('quotes.txt') as file:

    quotes = [i for i in file.readlines()]
    choice = random.choice(quotes)
    print(choice)


now = dt.datetime.now()
today = now.weekday()
if today == 2:
    print('wendsday')
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='mau_menezes@yahoo.com', msg=f'Subject: Quotes \n\n {choice}')
