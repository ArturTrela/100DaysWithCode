from tkinter import *
import random
# -------------------------- CONSTANTS-------------------------------------------#
BACKGROUND = "#9EB8D9"
FOREGROUND = "#7C93C3"
FONTNAME = "Times New Roman "
datalist=[]
upLetterList =[]
PASSWORDLENGHT = 16
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9''!', '#', '$', '%',
        '&', '(', ')', '*', '+', '-',  '/', '<', '=', '>', '?', '@', '[', ']', '^', '_']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    new_password = []
    for i in range(0,PASSWORDLENGHT):
        pointer = random.randrange(0,len(char))
        sign = char[pointer]
        new_password.append(sign)

    final_pass = ''.join(str(sign) for sign in new_password)
    if len(password_Field.get())==0:
        password_Field.insert(0, final_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    web = website_Input.get()
    user = username_Input.get()
    password = password_Field.get()
    data = (f"WEB: {web}    |    USERNAME : {user}  |  PASSWORD: {password}\n ")
    datalist.append(data)
    with open("data.txt", "a") as file:
        file.writelines(datalist)
    # Clear field after insert data into file


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(background=BACKGROUND, pady=20, padx=20)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=False)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=0, row=0, columnspan=3)

website_Label = Label(text="Website :", font=(FONTNAME, 10, "bold"), bg=BACKGROUND)
website_Label.grid(column=0, row=1)

username_Label = Label(text="Username / mail :", font=(FONTNAME, 10, "bold"), bg=BACKGROUND)
username_Label.grid(column=0, row=2)

password_Label = Label(text="Password", font=(FONTNAME, 10, "bold"), bg=BACKGROUND)
password_Label.grid(column=0, row=3)

website_Input = Entry(width=40, highlightbackground=FOREGROUND)
website_Input.grid(column=1, row=1, columnspan=2, sticky="w")
website_Input.focus()
username_Input = Entry(width=40, fg=FOREGROUND)
username_Input.grid(column=1, row=2, columnspan=2, sticky="w")
username_Input.insert(0,"testmail@elephant.com")
password_Field = Entry(width=21, )
password_Field.grid(column=1, row=3, sticky="w")

generate_Button = Button(width=15,text="Generate Password", highlightcolor="blue", command=generate)
generate_Button.grid(column=1, row=3, padx=131)

add_Button = Button(width=34, text="ADD", padx=0, command=save)
add_Button.grid(column=1, row=4, sticky="w")

screen.mainloop()
