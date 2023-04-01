"""imported Screen class form the turtle module"""
from turtle import Screen

"""created screen object"""
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.bgcolor("black")

"""screen will exit on click"""
screen.exitonclick()