import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("circle")
        self.color("SlateGrey")
        self.x_direction = 10
        self.y_direction = 10
        self.move_speed = 0.2

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_direction *= -1

    def x_bounce(self):
        self.x_direction *= -1
        self.move_speed *= 0.9
        
    def generate_y_direction(self):
        y = random.randint(0, 1)
        if y == 0:
            return 10
        elif y == 1:
            return -10

    def reset(self, player):
        self.goto(0, 0)
        self.move_speed = 0.16
        if player == "right":
            self.x_direction = 10
            self.generate_y_direction()
        elif player == "left":
            self.x_direction = -10
            self.generate_y_direction()
