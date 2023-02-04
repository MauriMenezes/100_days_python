import time
import math
import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_mark.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text='REST', fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        title_label.config(text='REST', fg=RED)
        count_down(short_break_sec)

    else:
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def add_marker():
    mark = ''
    work_sessions = math.floor(reps/2)
    print(reps)
    print(f'{work_sessions=}')
    for i in range(work_sessions):
        print(i)
        mark += '✔'
    check_mark.config(text=mark)


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
        add_marker()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# label TIMER
title_label = tkinter.Label(text='TIMER', font=(
    FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)
# button Start
button_start = tkinter.Button(
    text='Start', command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)
# button Reset
button_reset = tkinter.Button(
    text='Reset', command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)
# check mark
check_mark = tkinter.Label(text='', fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
