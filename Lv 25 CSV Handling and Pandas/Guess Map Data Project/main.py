import turtle
import pandas
from turtle import Turtle

SOURCE_IMG = "Lv 25 CSV Handling and Pandas/Guess Map Data Project/blank_states_img.gif"
SOURCE_DATA = "Lv 25 CSV Handling and Pandas/Guess Map Data Project/50_states.csv"
TARGET_DATA = "Lv 25 CSV Handling and Pandas/Guess Map Data Project/Missing_States_Data.csv"

screen = turtle.Screen()
screen.title("Guessing Map Game")
screen.addshape(SOURCE_IMG)
turtle.shape(SOURCE_IMG)
current_state = Turtle()
quiz_data = pandas.read_csv(SOURCE_DATA)
all_states = quiz_data.state.to_list()
guessed_states = []
missing_states = []

# checking Coordinates of Mouseclicks on Game Screen
# def get_mouse_click_cor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_cor)

def get_state_coordinates(answer):
    row = quiz_data[quiz_data.state == answer]
    return int(row.x), int(row.y)

def create_missing_states():
    # for state in all_states:
    #     if state not in guessed_states:
    #         missing_states.append(state)
    missing_states = [state for state in all_states if state not in guessed_states]

    missing_states_dataframe = pandas.DataFrame(missing_states)
    missing_states_dataframe.to_csv(TARGET_DATA)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess next State")
    answer_state = answer_state.title()
    
    if answer_state == "Exit":
        create_missing_states()
        break

    if answer_state in all_states and answer_state not in guessed_states:
        current_x ,current_y = get_state_coordinates(answer_state)
        current_state.hideturtle()
        current_state.penup()
        current_state.setposition(current_x,current_y)
        current_state.write(answer_state)
        guessed_states.append(answer_state)

# turtle.mainloop()