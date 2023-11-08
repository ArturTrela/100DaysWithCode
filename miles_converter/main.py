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
    user_input = (inputField.get())
    print(user_input)
    result = user_input

    return result

convertButton = Button(width=10, height=1, foreground="gray", background="White", font=("Arial", 10, "bold"),
                       text="Convert", command= convert)
convertButton.grid(column=1, row=5)

resultLabel =Label( text= " Your result is equal : ")
resultLabel.grid(column=0, row=5)

outputField =Text()
outputField.insert(END, convert())
outputField.grid(column = 0, row=10)
outputField.config(width=15 , height= 1)



window.mainloop()
