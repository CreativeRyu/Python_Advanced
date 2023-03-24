from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 30, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.left_score}  {self.right_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        self.clear()
        if player == "right":
            self.right_score += 1
        if player == "left":
            self.left_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
