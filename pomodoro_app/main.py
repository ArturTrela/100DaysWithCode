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
status = ["WORK", "BREAK"]
worktime_preset = 25
breaktime_preset = 5
pomodoro_is_On = True
remaining_time = datetime.time(0, 25, 0)

window = tk.Tk()
window.image ="tomato.png"
window.title("POMODORO APP")
window.minsize(240, 480)

# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# act_time = datetime.time(0, minutes, seconds)
def down():
    minutes = 24
    seconds = 59
    while minutes >0:
        for y in range(0,seconds):
            time.sleep(0.1)
            seconds -=1
            remaining_time = (f'{minutes} : {seconds}')
            print(remaining_time)
        minutes -= 1

    print(minutes)

#
# # ---------------------------- TIMER RESET ------------------------------- #

# # ---------------------------- TIMER MECHANISM ------------------------------- #

# # ---------------------------- UI SETUP ------------------------------- #
#
window.img = PhotoImage(file=window.image)
label = tk.Label(window, image=window.img)
label.grid(column=4, row=1)

title_label = tk.Label(text=status[0], font=FONT_NAME)
title_label.config(padx=0, pady=0)
title_label.grid(column=4, row=0)

start_btn = tk.Button(text="START", background=PINK, foreground="Black", font=FONT_NAME,command=down)
start_btn.grid(column=2, row=5)

reset_btn = tk.Button(text="RESET", background=PINK, foreground="Black", font=FONT_NAME, )
reset_btn.grid(column=8, row=5)

time_label = tk.Label(text = remaining_time, font=FONT_NAME, )
time_label.grid(column=4, row=1)


window.mainloop()
