# ___________IMPORTS_______________#

from tkinter import *
import pandas
import random
import time

# __________CONSTANT_________#
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
clockApp = None

current_card = {}
missing = []
known = []
pointer = 0

# ____________BACKGROUND LOGIC___________________#
data = pandas.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")


def next_word():
    global clockApp, background_card, pointer, current_card
    current_card = random.choice(data_dict)
    canvas.itemconfig(background_card, image=imageCardFront)
    canvas.itemconfig(canvas_language, text="French")

    next_word_fr = current_card["French"]
    canvas.itemconfig(canvas_word, text=next_word_fr)
    clockApp = screen.after(3000, flip_card)


def unknown_clicked():
    missing.append(current_card)
    next_word()


def known_clicked():
    known.append(current_card)
    next_word()
    data_dict.remove(current_card)


def flip_card():
    global clockApp
    next_word_en = current_card["English"]
    canvas.itemconfig(background_card, image=imageCardBack)
    canvas.itemconfig(canvas_language, text="English")
    canvas.itemconfig(canvas_word, text=next_word_en)


def save_scores():
    missingDf = pandas.DataFrame(data_dict)
    missingDf.to_csv("missing_words.csv", index=False)

    knownDf = pandas.DataFrame(known)
    knownDf.to_csv("known_words.csv", index=False)


# __________GUI SETUP______________________#
screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flash Card")
canvas = Canvas(width=800, height=526, highlightthickness=False, bg=BACKGROUND_COLOR)
imageCardFront = PhotoImage(file="./images/card_front.png")
imageCardBack = PhotoImage(file="./images/card_back.png")
background_card = canvas.create_image(400, 264, image=imageCardFront)
canvas.grid(column=0, row=0, columnspan=2)
canvas_language = canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT, fill="black")
canvas_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT, fill="black")

wrong_icon = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_icon, highlightthickness=False, command=unknown_clicked)
unknown_button.grid(column=0, row=1)

right_icon = PhotoImage(file="./images/right.png")
known_button = Button(image=right_icon, command=known_clicked)
known_button.grid(column=1, row=1)

print(next_word)
screen.mainloop()

save_scores()
