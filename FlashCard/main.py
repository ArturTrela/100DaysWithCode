from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flash Card")
canvas = Canvas(width=800, height=828, highlightthickness=False, bg=BACKGROUND_COLOR)
imageCardFront = PhotoImage(file="./images/card_front.png")
imageCardBack = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 264, image=imageCardFront)
canvas.grid(column=1, row=1, columnspan=2)
canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black")
canvas.create_text(400, 263, text="WORD", font=WORD_FONT, fill="black")

right_icon = PhotoImage(file="./images/right.png")
canvas.create_image(600, 600, image=right_icon)

wrong_icon = PhotoImage(file="./images/wrong.png")
canvas.create_image(200, 600, image=wrong_icon)


screen.mainloop()
