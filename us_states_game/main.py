import pandas
import pandas as pd
import turtle
from writer import Writer
import time
ALIGMENT = "center"
FONT = ('Arial', 8, 'normal')

screen = turtle.Screen()
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
input_data = pd.read_csv("50_states.csv")
# print(input_data)
question_num = 0
correct_answer=[]
table_states = []
writer = Writer()
popUp =Writer()
while question_num < 51:
    answer_state = (screen.textinput(prompt="What's next state?", title=f'{question_num}/50 States Correct')).title()
    next_state = (input_data.state == answer_state)
    for state in input_data.state:
        table_states.append(state)
    if answer_state in table_states:
        for_cords = input_data[next_state]
        # print(for_cords)
        x_cord = int(for_cords["x"])
        y_cord = int(for_cords["y"])

        writer.goto(int(x_cord), int(y_cord))
        writer.write(answer_state, move=False, align=ALIGMENT, font=FONT)
        screen.update()
        correct_answer.append(answer_state)


    else:
        popUp.goto(0,0)
        popUp.write("Wrong state name", move=False, align=ALIGMENT,font=("Tahoma", 42, "bold"))
        time.sleep(2)
        popUp.clear()

    question_num += 1
    missing_states = [state for state in input_data.state if state not in correct_answer]
    last_values = pandas.DataFrame(correct_answer)
    last_values.to_csv("last_values.csv")
    missing_df = pd.DataFrame(missing_states)
    missing_df.to_csv("missing_states.csv")
screen.exitonclick()
