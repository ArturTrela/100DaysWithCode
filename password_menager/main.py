from tkinter import *
#-------------------------- CONSTANTS-------------------------------------------#
BACKGROUND = "#9EB8D9"
FOREGROUND = "#7C93C3"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(background=BACKGROUND)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=640 , height=480, bg=BACKGROUND)
canvas.create_image(320,100, image= lock_image)
canvas.grid(column=2, row=2)



screen.mainloop()