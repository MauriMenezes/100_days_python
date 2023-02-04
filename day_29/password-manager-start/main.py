import tkinter as ttk
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    # pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = w_input.get()
    email = user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title='Oops', message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                json_data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            json_data.update(new_data)

            # Saving updated data
            with open('data.json', 'w') as data_file:
                json.dump(json_data, data_file, indent=4)
        finally:
            w_input.delete(0, ttk.END)
            password_input.delete(0, ttk.END)

#--------------------------- SEACH PASSWORD --------------------------- #


def find_password():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='WARNING', message='NO DATA FILE FOUND!')
    else:
        input_user = w_input.get()
        try:
            found_data = data[input_user]
        except KeyError:
            messagebox.showinfo(title='WARNING', message='NO FILE FOUND')
        else:
            email = found_data['email']
            password = found_data['password']

            messagebox.showinfo(
                title="FOUND", message=f'EMAIL : {email}\n PASSWORD : {password}')
        finally:
            w_input.delete(0, ttk.END)
            password_input.delete(0, ttk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = ttk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)


canvas = ttk.Canvas(width=200, height=200)
img = ttk.PhotoImage(file='logo.png')

canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#  website
w_label = ttk.Label(text='Website : ')
w_label.grid(column=0, row=1)
w_input = ttk.Entry()
w_input.config(width=30)
w_input.grid(column=1, row=1, columnspan=1)
w_input.focus()

# Email/Username
user_label = ttk.Label(text='Email/Username : ')
user_label.grid(column=0, row=2)
user_input = ttk.Entry()
user_input.config(width=45)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, 'mauriliosm25@gmail.com')

# label Password

password_label = ttk.Label(text='Password :')
password_label.grid(column=0, row=3)
password_input = ttk.Entry()
password_input.config(width=28)
password_input.grid(column=1, row=3)

# btns

# GENERATE PASSWORD BTN
password_btn = ttk.Button(text='Generate', width=16, command=generate_password)
password_btn.grid(column=2, row=3)

# ADD BTN
add_btn = ttk.Button(text='Add', command=save, width=45)
add_btn.grid(row=4, column=1, columnspan=2)

# SEARCH BTN
search_btn = ttk.Button(text="Search", command=find_password, width=14)
search_btn.grid(column=2, row=1)
window.mainloop()
