import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(height=100, width=300)


def button_clicked():
    value = float(input.get())
    km = round((value * 1.609), 2)

    label_3.config(text=km)


# Entry
input = tkinter.Entry(width=15)
print(input.get())
input.grid(column=1, row=0)
# Label
label_1 = tkinter.Label(
    text='Miles ', font=('Arial', 15, 'bold'))
label_1.grid(column=2, row=0)
label_2 = tkinter.Label(
    text='is equal to ', font=('Arial', 15, 'bold'))
label_2.grid(column=0, row=1)
label_3 = tkinter.Label(
    text='0', font=('Arial', 15, 'bold'))
label_3.grid(column=1, row=1)
label_4 = tkinter.Label(
    text='km', font=('Arial', 15, 'bold'))
label_4.grid(column=2, row=1)

# button
button = tkinter.Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=3)
# # # 2° button
# button = tkinter.Button(text='Not Him Me', command=button_clicked)
# button.grid(column=2, row=0)

window.mainloop()
