"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""ball's initial moving direction"""
BALL_DIRECTION = 45
"""ball's forward distance"""
BALL_DISTANCE = 40

"""created Ball class"""
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.setheading(BALL_DIRECTION)
        self.forward(BALL_DISTANCE)
