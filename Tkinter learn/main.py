import tkinter
from tkinter import END

window = tkinter.Tk()
window.title(" First GUI Program")
window.wm_minsize(640,480)
window.wm_maxsize(1080,700)
window.config(padx=20 ,pady =20)

# Label

my_label =tkinter.Label(text="Label example",font =("Arial" , 24 , "bold"))
my_label.grid(column = 2, row=3 )
#

my_label["text"] = "Text Label"
my_label.config(text="New Text")


#  Button

def btn_click():
    nowy_text = input.get()
    my_label.config(text=nowy_text)

button = tkinter.Button(text="Click me!", background="pink",foreground="Black",font=("Arial", 20 , "bold" ), command=btn_click)
button.grid(column= 0, row =0)

new_button = tkinter.Button(text= "new button")
new_button.grid(column =2, row=3 )
#Entry

input = tkinter.Entry(width=30, background="silver")
input.grid(column =1, row =1 )
#
""" EXAMPLE USING MANY OF TKINTER WIDGETS
#
# #Multiline input
#
# text_entry = tkinter.Text(width=30, height= 5 ,font=("Arial",12 , ))
# text_entry.focus()
# text_entry.insert(END ,"Example of multiline input field")
# print(text_entry.get("1.0", END))
# text_entry.pack()
#
#
# # spin box
#
# def spin_box_used():
# #     gets the current value in spinbox
#     print(spinbox.get())
# spinbox = tkinter.Spinbox(from_= 0, to =10 , width=5, command = spin_box_used)
# spinbox.pack()
#
#
#
# #Scale
# # Called with current scale value
#
# def scale_used(value):
#     print(value)
#
# scale = tkinter.Scale(from_=0, to=100, command= scale_used)
# scale.pack()
#
#
# # Check button
#
# def check_button_used():
# #     Prints 1 if button ON otherwise 0
#     print(checked_state.get())
# # variable to hold on in checked state 0 is off 1 is On
# checked_state =tkinter.IntVar()
# checkButton = tkinter.Checkbutton(text = "It'On ?",variable = checked_state,command = check_button_used)
# checked_state.get()
# checkButton.pack()
#
#
# #Radio Button
#
# def radio_button_used():
#     print(radio_state.get())
# #  Variable to hold on to which radio button value is checked
# radio_state  =tkinter.IntVar()
# radio_btn1 = tkinter.Radiobutton(text = "Option 1", value=1, variable=radio_state,command=radio_button_used)
# radio_btn2 = tkinter.Radiobutton(text = "Option 2", value=2, variable=radio_state,command=radio_button_used)
#
# radio_btn1.pack()
# radio_btn2.pack()
#
# # List box
#
# def listBox_used():
#     print(listBox.get(listBox.curselection()))
#
#
# listBox = tkinter.Listbox(height=6)
# fruits =["Apple","banana", "Pear"," Orange"]
# for f in fruits:
#     listBox.insert(fruits.index(f),f)
#
# listBox.bind("<<ListBox Select>>", listBox_used)
# listBox.pack()

"""
window.mainloop()