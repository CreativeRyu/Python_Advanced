from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("square")
        self.color("SlateGrey")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.goto(position)

    # Steuerung für ein Paddle
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
