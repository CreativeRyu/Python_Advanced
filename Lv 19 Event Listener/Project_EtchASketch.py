# # # # Lv 19 Project 01 Etch-A-Sketch # # # #
from turtle import Turtle,Screen

my_dude = Turtle()
screen = Screen()

def move_forwards():
    my_dude.forward(10)

def move_backwards():
    my_dude.backward(10)

def turn_clockwise():
    my_dude.right(10)
    
def turn_counterclockwise():
    my_dude.left(10)

def clear_screen():
    my_dude.clear()
    my_dude.penup()
    my_dude.home()
    my_dude.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_counterclockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
