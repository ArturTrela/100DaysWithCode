from tkinter import *
#-------------------------- CONSTANTS-------------------------------------------#
BACKGROUND = "#9EB8D9"
FOREGROUND = "#7C93C3"
FONTNAME = "Times New Roman "
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(background=BACKGROUND, pady=20,padx=20)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200 , height=200, bg=BACKGROUND, highlightthickness=False)
canvas.create_image(100,100, image= lock_image )
canvas.grid(column=0, row=0, columnspan =3)

website_Label = Label(text="Website :", font=(FONTNAME,10,"bold"),bg=BACKGROUND)
website_Label.grid(column=0, row=1)

username_Label = Label(text="Username / mail :", font=(FONTNAME,10,"bold"),bg=BACKGROUND)
username_Label.grid(column=0, row=2)

password_Label = Label(text="Password", font=(FONTNAME,10,"bold"),bg=BACKGROUND)
password_Label.grid(column=0, row=3)

website_Input = Entry(width=40 ,highlightbackground=FOREGROUND)
website_Input.grid(column =1, row =1 , columnspan = 2,sticky="w")

username_Input = Entry(width=40)
username_Input.grid(column =1, row =2 , columnspan = 2,sticky="w")

password_Field = Entry(width=21, )
password_Field.grid(column =1, row =3 ,sticky="w")

generate_Button = Button(width=15, text="Generate Password", highlightcolor="blue", command='')
generate_Button.grid(column =1, row =3,padx=131)

add_Button = Button(width=34, text="ADD",padx=0)
add_Button.grid(column =1, row =4 ,sticky="w")

screen.mainloop()