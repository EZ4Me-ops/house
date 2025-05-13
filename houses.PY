import turtle
from turtle import *

pen=turtle.Turtle()
screen = turtle.Screen()

def truangle(x, y, colour, side):
  pen.penup()
  pen.goto(x, y)
  pen.pendown()
  pen.color(colour)
  pen.begin_fill()
  for i in range(3):
    pen.forward(side)
    pen.left(120)
  pen.end_fill()
truangle(0, 0, "orange", 50)
def sqauure(x, y, colour, side):
  pen.penup()
  pen.goto(x, y)
  pen.pendown()
  pen.color(colour)
  pen.begin_fill()
  for i in range(4):
    pen.forward(side)
    pen.right(90)
sqauure(0, 0, "crimson", 50)
truangle(-100, -100, "", 70)
sqauure(-100, -100, "green", 70)


turtle.done()