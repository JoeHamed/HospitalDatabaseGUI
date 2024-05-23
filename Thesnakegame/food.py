from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.refresh()
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.speed(0)       # Fastest Speed

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)
