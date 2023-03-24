from colorthief import ColorThief
from turtle import Turtle, Screen
import turtle
import random

my_dude = Turtle()
screen = Screen()
screen.bgcolor("gray10")
my_dude.speed(10)
turtle.colormode(255)
my_dude.hideturtle()
my_dude.penup()
my_dude.goto(-230, -210)
# Extract Colors from an image

# color_thief = ColorThief('E:/BILDER/PixelRyu.PNG')
color_thief = ColorThief(
    'D:/UNTERRICHTSPLANUNG/Python/Python_Learn_Modules/Lv 18 Graphical UI/Project_ColorDropMatrix/SonicFrontiers.jpg')
# Dominanteste Farbe abgreifen
# dominant_color = color_thief.get_color(quality = 1)

# Farbpalette mit x Farben abgreifen
color_palette = color_thief.get_palette(color_count=20)


# Es sollen 10 x 10 Punkte gezeichnet werden
# Die Punkte sollen eine Größe von 20 und einen Abstand von 50 zueinander haben

# # gestrichelte Linie zeichnen

for line in range(10):
    ycor = my_dude.ycor()
    xcor = my_dude.xcor()
    for dots in range(10):
        my_dude.pendown()
        color_drop = random.choice(color_palette)
        my_dude.pencolor(color_drop)
        my_dude.dot(20)
        my_dude.penup()
        my_dude.fd(50)
    ycor = ycor + 50
    my_dude.goto(xcor, ycor)
    
screen.exitonclick()
