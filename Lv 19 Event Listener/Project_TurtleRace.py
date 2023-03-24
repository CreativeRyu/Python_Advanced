# # # # Lv 19 Project 02 Turtle Race # # # #
import random
from turtle import Turtle, Screen

# Setup Variables and Objects
screen = Screen()
screen.setup(width=700, height=400)
screen.bgcolor("lemonchiffon2")
user_bet = screen.textinput(title="Bet for Turtle Race", prompt="Welche Schildkröte wird das rennen machen? Geben Sie die Farbe ein: ")
x = -320
y = -130
colors = ["deepPink","crimson","darkorange","gold","limegreen","dodgerblue","darkViolet"]
turtle_list = []
is_race_on = False

# Creates Turtles with Shape and Color
for color in colors:
    color_turtle = Turtle(shape="turtle")
    color_turtle.color(color)
    turtle_list.append(color_turtle)

"""
+================================+
|           Game Logic           |
+================================+
"""

# Place Turtles at Startline in the Game
for turtle in turtle_list:
    turtle.penup()
    turtle.goto(x, y)
    y += 40 

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 320:
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"Sie haben gewonnen Sir, die Schildkröte mit der Farbe {turtle.pencolor()} hat das Rennen gewonnen.")
            else: 
                print(f"Sie haben leider verloren Sir, die Schildkröte mit der Farbe {turtle.pencolor()} hat das Rennen gewonnen.")
                
            is_race_on = False


screen.exitonclick()
