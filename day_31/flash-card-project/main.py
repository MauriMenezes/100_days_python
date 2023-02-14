from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# reading csv

data = pandas.read_csv('data/german_words.csv')
dict_data = data.to_dict(orient='records')
try:
    unknow_words = pandas.read_csv('data/words_to_review.csv')
except FileNotFoundError:
    data = pandas.DataFrame([])
    data.to_csv("data/words_to_review.csv")
unknow_dict = unknow_words.to_dict(orient='records')

current_card = {}


def next_card():
    global current_card, window_timer
    window.after_cancel(window_timer)
    print(current_card)

    current_card = random.choice(dict_data)
    if current_card not in unknow_dict:
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(card_title, text='German', fill="black")
        canvas.itemconfig(card_word, text=current_card['German'], fill="black")
        window_timer = window.after(4000, flip_card)

# //////


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


def is_unknow():
    try:
        df = pandas.DataFrame({
            'English': [current_card['English']],
            'German': [current_card['German']]
        })
        df.to_csv('data/words_to_review.csv',
                  mode='a', index=False, header=False)
    except FileNotFoundError:
        words = {
            'English': [current_card['English']],
            'German': [current_card['German']]
        }
        data = pandas.DataFrame(words)
        data.to_csv("data/words_to_review.csv")

    next_card()


def is_known():
    ...


def review():

    ...


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window_timer = window.after(3000, flip_card)


# /////// UI ////////
back_card_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, 'bold'))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")

wrong_btn = Button(image=x_image, command=is_unknow)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=check_image, command=next_card)
right_btn.grid(row=1, column=1)

revisar_btn = Button(text='revisar', command=review)
revisar_btn.grid(row=2, column=0)

next_card()
window.mainloop()
