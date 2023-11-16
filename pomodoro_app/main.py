import tkinter
import tkinter as tk
from tkinter import PhotoImage
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 24,)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
status = ["WORK", "BREAK", "LONG BREAK"]
pomodoro_qty = ['', '✔', '', '✔✔', '', '✔✔✔', '', '✔✔✔✔', '', '✔✔✔✔✔']
mark = "✔"
reps = 0
clockApp = None


# # ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(clockApp)
    reps = 0
    pomodoro_label.config(text=pomodoro_qty[0])
    canvas.itemconfig(timer_text, text=f'00:00')



# # ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        title_label.config(text=status[0], fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        title_label.config(text=status[1], fg=PINK)
        pomodoro_label.config(text=pomodoro_qty[reps - 1])
    elif reps == 8:
        count_down(long_break_sec)
        title_label.config(text=status[2], fg=RED)
        pomodoro_label.config(text=pomodoro_qty[reps - 1])
    else:
        pass

    print(reps)


# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global clockApp
    count_min = math.floor(count / 60)
    count_sec = round(count % 60)
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count >= 0:
        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
        clockApp = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# # ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("POMODORO APP")
window.config(padx=100, pady=50, background=YELLOW)
canvas = tkinter.Canvas(width=201, height=223, bg=YELLOW, highlightthickness=False)
backgroundImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=backgroundImage)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=2, row=2)

title_label = tk.Label(text=status[0], fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
title_label.config(padx=0, pady=0)
title_label.grid(column=2, row=1)

start_btn = tk.Button(text="START", background=YELLOW, foreground=GREEN, highlightthickness=False,
                      font=(FONT_NAME, 12, "bold"), command=start_timer)
start_btn.grid(column=1, row=4)

reset_btn = tk.Button(text="RESET", background=YELLOW, foreground=GREEN, highlightthickness=False,
                      font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_btn.grid(column=3, row=4)

pomodoro_label = tk.Label(text=pomodoro_qty[reps], background=YELLOW, foreground=GREEN, font=FONT_NAME, )
pomodoro_label.grid(column=2, row=5)

window.mainloop()
