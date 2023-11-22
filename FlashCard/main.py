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
next_word_fr = ""
next_word_en = ""
missing = []
known = []
pointer = 0
# ____________BACKGROUND LOGIC___________________#
data = pandas.read_csv("./data/french_words.csv")
table_long = 100


def next_word():
    global next_word_fr, clockApp, background_card, pointer
    canvas.itemconfig(background_card, image=imageCardFront)
    canvas.itemconfig(canvas_language, text="French")
    pointer = random.randrange(0, len(data))
    next_word_fr = data["French"][pointer]
    canvas.itemconfig(canvas_word, text=next_word_fr)
    clockApp = screen.after(3000, flip_card)
    print(next_word_fr)


def unknown_clicked():
    global next_word_fr, missing
    missing.append(next_word_fr)
    next_word()


def known_clicked():
    global next_word_fr, known
    known.append(next_word_fr)
    next_word()


def flip_card():
    global clockApp, next_word_en
    next_word_en = data["English"][pointer]
    canvas.itemconfig(background_card, image=imageCardBack)
    canvas.itemconfig(canvas_language, text="English")
    canvas.itemconfig(canvas_word, text=next_word_en)


def save_scores():
    global missing, known
    missingDf = pandas.DataFrame(missing)
    missingDf.to_csv("missing_words.csv")

    knownDf = pandas.DataFrame(known)
    knownDf.to_csv("knows_words.csv")


# __________GUI SETUP______________________#
screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flash Card")
canvas = Canvas(width=800, height=526, highlightthickness=False, bg=BACKGROUND_COLOR)
imageCardFront = PhotoImage(file="./images/card_front.png")
imageCardBack = PhotoImage(file="./images/card_back.png")
background_card = canvas.create_image(400, 264, image=imageCardFront)
canvas.grid(column=0, row=0, columnspan=2)
canvas_language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black")
canvas_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT, fill="black")

wrong_icon = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_icon, highlightthickness=False, command=unknown_clicked)
unknown_button.grid(column=0, row=1)

right_icon = PhotoImage(file="./images/right.png")
known_button = Button(image=right_icon, command=known_clicked)
known_button.grid(column=1, row=1)



print(next_word)
save_scores()
screen.mainloop()
