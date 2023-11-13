import tkinter as tk
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 48 , )
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
status =["WORK","BREAK"]

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
class Window:

    def __init__(self, image):
        self.image = image
        self.root = tk.Tk()
        self.root.title("POMODORO APP")
        self.root.minsize(240, 480)
        self.widgets()
        self.root.mainloop()

    def widgets(self):
        self.img = PhotoImage(file=self.image)
        label = tk.Label(self.root, image=self.img)
        label.config(padx=0,pady=0)
        label.grid(column=1, row=1)

        title_label = tk.Label(text=status[0], font=FONT_NAME)
        title_label.config(padx=0,pady=0)
        title_label.grid(column=1, row=0)

        start_btn = tk.Button(text = "START! ", background=PINK, foreground="Black", font=FONT_NAME)

        start_btn.grid(column=1, row=2)


image = "tomato.png"
Window(image)
