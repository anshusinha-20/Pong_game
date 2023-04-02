"""imported Screen class form the turtle module"""
from turtle import Screen

"""imported time module"""
import time

"""imported Paddle class from the paddle module"""
from paddle import Paddle

"""imported Ball class from the ball module"""
from ball import Ball

"""paddle positions"""
RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)

"""created screen object"""
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

"""created paddleRight object"""
paddleRight = Paddle(RIGHT_POS)

"""created paddleLeft object"""
paddleLeft = Paddle(LEFT_POS)

"""created ball object"""
ball = Ball()

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
    """screen's animation and delay"""
    screen.update()
    time.sleep(0.08)

    """ball's movement"""
    ball.move()

    """detecting collision with the walls"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

"""screen will exit on click"""
screen.exitonclick()