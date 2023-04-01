"""imported Screen class form the turtle module"""
from turtle import Screen

"""imported Paddle class from the paddle module"""
from paddle import Paddle

"""created screen object"""
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

"""created paddleRight object"""
paddleRight = Paddle()
paddleRight.goto(350, 0)

"""created paddleLeft object"""
paddleLeft = Paddle()
paddleLeft.goto(-350, 0)

"""paddleRight moves on pressing the up and down arrow keys"""
screen.onkey(paddleRight.up, "Up")
screen.onkey(paddleRight.down, "Down")

"""paddleLeft moves on pressing the w and s keys"""
screen.onkey(paddleLeft.up, "w")
screen.onkey(paddleLeft.down, "s")

"""variable to hold the game running condition"""
isGameOn = True

"""until the game is on the loop runs"""
while isGameOn:
    screen.update()

"""screen will exit on click"""
screen.exitonclick()