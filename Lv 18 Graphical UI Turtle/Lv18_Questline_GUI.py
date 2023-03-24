# # # # Lv 18 GUI mit Turtle # # # #
from turtle import Turtle, Screen
import random
import turtle


my_dude = Turtle()
screen = Screen()

my_dude.shape("turtle")
my_dude.color("DarkSeaGreen")
screen.bgcolor("gray10")
color_list = ["aquamarine", "aquamarine4", "bisque4", "blue", "BlueViolet", "brown1", "CadetBlue1", "chartreuse", "chartreuse4", "chocolate", "coral2",
              "DarkOliveGreen3", "DarkGoldenrod1", "DarkGreen", "DarkOrange1", "DarkRed", "DarkSeaGreen3", "DarkSlateGray", "DeepPink2", "DarkTurquoise", "DeepSkyBlue"]

# # ein Viereck zeichnen
# for _ in range(4):
#     my_dude.forward(100)
#     my_dude.left(90)


# # gestrichelte Linie zeichnen
# for _ in range(4):
#     my_dude.fd(25)
#     my_dude.penup()
#     my_dude.fd(25)
#     my_dude.pendown()

"""
+================================+
|                                |
|       Lv 18 Multishapes        |
|                                |
+================================+
"""

# multiple Figuren zeichnen


def draw_multishapes(sides):
    my_dude.pensize(5)
    while sides < 11:
        for _ in range(sides):
            pen_color = random.choice(color_list)
            my_dude.pencolor(pen_color)
            angle = 360 / sides
            my_dude.fd(100)
            my_dude.left(angle)
        sides += 1


sides = 3
draw_multishapes(sides)

# -----------------------------------------------------------------------------

"""
+================================+
|                                |
|       Lv 18 Random Walk        |
|                                |
+================================+
"""

compass = [0, 90, 180, 270]
my_dude.pensize(10)
my_dude.speed(10)


def random_walk():
    for walk in range(200):
        direction = random.choice(compass)
        turtle_color = random.choice(color_list)
        my_dude.color(turtle_color)
        # Set Heading lässt die Turtle in die vom Winkel angegebene Richtung schauen
        my_dude.setheading(direction)
        my_dude.forward(50)
        walk += 1


random_walk()

# -----------------------------------------------------------------------------

"""
+================================+
|                                |
|          Lv 18 Tuple           |
| Um random Colors zu generieren |
+================================+
"""

my_tuple = (1, 3, 8)
my_tuple[2] # würde die 8 ausgeben
# Unterschied zur normalen Liste ist, 
# dass ein Tupel in Stein gemeißelt ist und die Werte darin niciht merh verändert werden können
# Immutable

# -----------------------------------------------------------------------------

"""
+================================+
|                                |
|        Lv 18 Random Walk       |
|mit zufällig generierten Farben |
+================================+
"""
turtle.colormode(255)

def random_RGB_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk():
    for walk in range(200):
        direction = random.choice(compass)
        my_dude.color(random_RGB_color())
        # Set Heading lässt die Turtle in die vom Winkel angegebene Richtung schauen
        my_dude.setheading(direction)
        my_dude.forward(50)
        walk += 1


random_walk()

# -----------------------------------------------------------------------------

"""
+================================+
|                                |
|        Lv 18 Spinagraph        |
|                                |
+================================+
"""

def draw_spinograph():
    for angle in range(1, 360, 10):  
        my_dude.pencolor(random_RGB_color())
        my_dude.setheading(angle)
        my_dude.circle(100)

draw_spinograph()




screen.exitonclick()