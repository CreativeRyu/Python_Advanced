# # # # Lv 19 Event Listener # # # #
from turtle import Turtle, Screen

my_dude = Turtle()
screen = Screen()

def move_forwards():
    my_dude.forward(10)

"""
+================================+
|                                |
|      Lv 19 Eventlistener       |
|     Higher Order Functions     |
+================================+
"""
# Eine Funktion die mit anderen Funktionen als Parameter arbeitet wird als Higher Order Function
# Bzw. Funktion höherer Ordnung bezeichnet

screen.listen()
screen.onkey(key="space", fun=move_forwards) # Wenn die Klammern mit übergeben werden, triggert das die Funktion
screen.exitonclick()
