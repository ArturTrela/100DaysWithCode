# ___________IMPORTS_______________#

from tkinter import *
import pandas

# __________CONSTANT_________#
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# __________GUI SETUP______________________#
screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flash Card")
canvas = Canvas(width=800, height=526, highlightthickness=False, bg=BACKGROUND_COLOR)
imageCardFront = PhotoImage(file="./images/card_front.png")
imageCardBack = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 264, image=imageCardFront)
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black")
canvas.create_text(400, 263, text="WORD", font=WORD_FONT, fill="black")


wrong_icon = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_icon, highlightthickness=False)
unknown_button.grid(column=0, row=1)

right_icon = PhotoImage(file="./images/right.png")
known_button = Button(image=right_icon, )
known_button.grid(column=1, row=1)

# ____________BACKGROUND LOGIC___________________#
data = pandas.read_csv("./data/french_words.csv")
print(data)
screen.mainloop()
