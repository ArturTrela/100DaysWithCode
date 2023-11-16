import tkinter
import tkinter as tk
from tkinter import PhotoImage
import datetime , time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 24,)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
remaining_time = 25
status =["WORK", "BREAK"]

# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# # ---------------------------- TIMER RESET ------------------------------- #

# # ---------------------------- TIMER MECHANISM ------------------------------- #

# # ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("POMODORO APP")
# window.minsize(240, 240)
window.config(padx=100 , pady=50 , background= YELLOW)
canvas = tkinter.Canvas(width=201 , height=223, bg=YELLOW, highlightthickness=False)
backgroundImage = PhotoImage(file="tomato.png")
canvas.create_image(100,111, image=backgroundImage)
canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME, 36, "bold"))
canvas.pack()





window.mainloop()



# window.img = PhotoImage(file=window.image)
# label = tk.Label(window, image=window.img)
# label.grid(column=4, row=1)
#
# title_label = tk.Label(text=status[0], font=FONT_NAME)
# title_label.config(padx=0, pady=0)
# title_label.grid(column=4, row=0)
#
# start_btn = tk.Button(text="START", background=PINK, foreground="Black", font=FONT_NAME,command='')
# start_btn.grid(column=2, row=5)
#
# reset_btn = tk.Button(text="RESET", background=PINK, foreground="Black", font=FONT_NAME,command='' )
# reset_btn.grid(column=8, row=5)
#
# time_label = tk.Label(text = remaining_time, font=FONT_NAME, )
# time_label.grid(column=4, row=1)