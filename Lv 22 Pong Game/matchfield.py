from turtle import Turtle
RIGHT_SIDE = 350
LEFT_SIDE = -350
LINE_SIZE = 21


class Matchfield(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.pensize(5)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -300)
        self.draw_midline(LINE_SIZE)
        self.draw_outline(RIGHT_SIDE)
        self.draw_outline(LEFT_SIDE)

    def draw_midline(self, lineSize):
        for _ in range(16):
            self.pendown()
            self.goto(0, self.ycor() + lineSize)
            self.penup()
            self.goto(0, self.ycor() + lineSize)

    def draw_outline(self, side):
        self.penup()
        self.pensize(3)
        self.pencolor("SlateGrey")
        self.goto(side, -300)
        for _ in range(18):
            self.pendown()
            self.goto(side, self.ycor() + 10)
            self.penup()
            self.goto(side, self.ycor() + 25)
