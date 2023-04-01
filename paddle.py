"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""created Paddle class"""
class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def up(self):
        self.newYPositive = self.ycor() + 40
        self.goto(self.xcor(), self.newYPositive)

    def down(self):
        self.newYNegative = self.ycor() - 40
        self.goto(self.xcor(), self.newYNegative)
