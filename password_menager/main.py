import tkinter.messagebox
from tkinter import *
import random
import pyperclip
import json
# -------------------------- CONSTANTS-------------------------------------------#
BACKGROUND = "#9EB8D9"
FOREGROUND = "#7C93C3"
FONTNAME = "Times New Roman "
datalist = []
PASSWORDLENGHT = 16
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9''!', '#', '$', '%',
        '&', '(', ')', '*', '+', '-', '/', '<', '=', '>', '?', '@', '[', ']', '^', '_']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    new_password = []
    for i in range(0, PASSWORDLENGHT):
        pointer = random.randrange(0, len(char))
        sign = char[pointer]
        new_password.append(sign)

    final_pass = ''.join(str(sign) for sign in new_password)
    if len(password_Field.get()) == 0:
        password_Field.insert(0, final_pass)
        pyperclip.copy(final_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if len(website_Input.get()) != 0 and len(password_Field.get()) >= 16 and len(username_Input.get()) != 0:
        website = website_Input.get()
        user = username_Input.get()
        password = password_Field.get()
        new_data = {
            website: {
                "email": user,
                "password": password,
            }

        }
        data = (f"WEB: {website}    |    USERNAME : {user}  |  PASSWORD: {password}\n ")
        datalist.append(data)
        dane ={}
        try:
            with open("data.json", "r") as file:
                # reading old data
                dane = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                # create a file when is empty
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            dane.update(new_data)
            with open("data.json", "w") as file:
                # update a file
                json.dump(dane, file, indent=4)
        finally:
            # Clear field after insert data into file
            website_Input.delete(0, END)
            password_Field.delete(0, END)

        tkinter.messagebox.showinfo("Confirmation", f"New password for {website} added successful ")
    else:
        tkinter.messagebox.showerror("ERROR", "Please insert correct data ")


def find_password():
    with open ("data.json" , "r") as file:
        data2 = json.load(file)
    user_text = website_Input.get()
    try:
        to_show = data2[user_text]
        pass_to_show = to_show["password"]
    except KeyError:
        tkinter.messagebox.showerror("ERROR", f'Website  not Found')

    else:
        tkinter.messagebox.showinfo("Information", f'Password for {user_text} is: {pass_to_show}')
    finally:
        pass

# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(background=BACKGROUND, pady=20, padx=20)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=False)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=0, row=0, columnspan=3)

website_Label = Label(text="Website :", font=(FONTNAME, 10, "bold"), bg=BACKGROUND, )
website_Label.grid(column=0, row=1)

username_Label = Label(text="Username / mail :", font=(FONTNAME, 10, "bold"), bg=BACKGROUND)
username_Label.grid(column=0, row=2)

password_Label = Label(text="Password", font=(FONTNAME, 10, "bold"), bg=BACKGROUND)
password_Label.grid(column=0, row=3)

website_Input = Entry(width=22, highlightbackground=FOREGROUND ,fg=FOREGROUND, highlightthickness=1)
website_Input.grid(column=1, row=1, sticky="w")
website_Input.focus()
username_Input = Entry(width=39, fg=FOREGROUND)
username_Input.grid(column=1, row=2, columnspan=2, sticky="w")
username_Input.insert(0, "testmail@elephant.com")
password_Field = Entry(width=22,highlightthickness=1 ,fg=FOREGROUND )
password_Field.grid(column=1, row=3, sticky="w")

generate_Button = Button(width=16, text="Generate", font=(FONTNAME,7,"normal"),highlightcolor="blue", command=generate)
generate_Button.grid(column=1, row=3, padx=131)

add_Button = Button(width=33, text="ADD", padx=0, command=save)
add_Button.grid(column=1, row=4, sticky="w")

search_Button = Button(width=17, text="Search", font=(FONTNAME,7,"normal"),highlightcolor="blue", command=find_password)
search_Button.grid(column =1 , row=1)
screen.mainloop()
