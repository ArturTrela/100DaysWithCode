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
window.image ="tomato.png"
window.title("POMODORO APP")
window.minsize(240, 480)
#
window.img = PhotoImage(file=window.image)
label = tk.Label(window, image=window.img)
label.grid(column=4, row=1)

title_label = tk.Label(text=status[0], font=FONT_NAME)
title_label.config(padx=0, pady=0)
title_label.grid(column=4, row=0)

start_btn = tk.Button(text="START", background=PINK, foreground="Black", font=FONT_NAME,command='')
start_btn.grid(column=2, row=5)

reset_btn = tk.Button(text="RESET", background=PINK, foreground="Black", font=FONT_NAME,command='' )
reset_btn.grid(column=8, row=5)

time_label = tk.Label(text = remaining_time, font=FONT_NAME, )
time_label.grid(column=4, row=1)


window.mainloop()
