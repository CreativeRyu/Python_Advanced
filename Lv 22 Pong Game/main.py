from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard
from matchfield import Matchfield

UPPER_WALL = 285
LOWER_WALL = -285
LEFT_WALL = -380
RIGHT_WALL = 380
player = ""

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("DarkOliveGreen3")
screen.title("Legendary Pong Game")
screen.tracer(0)

matchfield = Matchfield()

# 1. Paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

# 2. Paddle Controls
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# Game Controller
is_game_on = True
while is_game_on:
    sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > UPPER_WALL or ball.ycor() < LOWER_WALL:
        ball.y_bounce()
        
    # Detect collision with Paddles
    if ball.distance(right_paddle) < 54 and ball.xcor() > 320 or ball.distance(left_paddle) < 54 and ball.xcor() < -320:
        ball.x_bounce()
    ball.move()

    if ball.xcor() == RIGHT_WALL:
        player = "left"
        score_board.increase_score(player)
        ball.reset(player)
    if ball.xcor() == LEFT_WALL:
        player = "right"
        score_board.increase_score(player)
        ball.reset(player)

screen.exitonclick()