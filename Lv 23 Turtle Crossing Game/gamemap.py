from turtle import Turtle


class GameMap(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.penup()
        self.color("#306230")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.draw_finishline(start_x=-292)
        self.draw_finishline(start_x=-304, start_y = 268)
        self.draw_street(0)
        self.draw_street(150)
        self.draw_street(-150)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def draw_finishline(self, start_x, start_y=280):
        self.goto(start_x, start_y)
        self.stamp()
        for _ in range(30):
            new_x = self.xcor() + 23
            self.goto(new_x, start_y)
            self.stamp()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def draw_street(self, start_y):
        self.hideturtle()
        self.color("#8bac0f")
        self.pensize(5)
        self.goto(-300, start_y)
        for _ in range(8):
            self.pendown()
            self.goto(self.xcor() + 50, start_y)
            self.penup()
            self.goto(self.xcor() + 30, start_y)