from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.speed(0)
        self.penup()
        self.color("#0f380f")
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move(self):
        self.forward(MOVE_DISTANCE)

    def reach_goal(self):
        if self.ycor() == FINISH_LINE_Y:
            # Turtle resetten
            # neues Level beginnen
            # autos beschleunigen
            pass