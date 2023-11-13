from tkinter import *

window = Tk()
window.title("Miles to kilometer converter")
window.config(width=200, height=100)
window.config(padx=15, pady=15)
window.minsize(300, 100)

title_label = Label(text="Miles to kilometers converter ")
title_label.grid(column=0, row=0)
title_label.config(padx=2)

inputField = Entry()
inputField.focus()
inputField.grid(column=0, row=3)


def convert():
    ratio = 1.609344
    user_input = inputField.get()
    result = float(user_input) * ratio
    print(result)
    resultLabel = Label(text=f' Your result is equal : {result} kilometers ')
    resultLabel.grid(column=0, row=5)


convertButton = Button(width=10, height=1, foreground="gray", background="White", font=("Arial", 10, "bold"),
                       text="Convert", command=convert)
convertButton.grid(column=1, row=5)



window.mainloop()
