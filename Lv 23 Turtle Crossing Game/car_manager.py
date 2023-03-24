from turtle import Turtle, Screen
import random


COLORS = ["#0f380f", "#306230"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid = 1.0, stretch_len=2.0)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        y_position = random.randint(-250, 250)
        new_car.goto(320, y_position)
        self.cars.append(new_car)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def automatic_drive(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
        