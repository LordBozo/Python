# circle.py
# set up the program
# import turtle drawing routines
from turtle import *
import random
# create the drawing window
setup()
# create a title for the drawing window
title("circles are fun")
# create a turtle to draw with
CircleBot = Turtle()
Color = 'Blue'
# draw the circle
# lift the pen up (away from the window)
# so it doesn't draw a line as it moves
while True:
    X = random.randrange(-350,350)
    Y = random.randrange(-350,350)
    CircleBot.up()
    # set the starting point for the drawing pen.
    CircleBot.goto(X,Y)
    # put the pen down (against the window) 
    # so it can begin to draw
    CircleBot.down()
    # set the pen color
    CircleBot.color(Color)
    # set the pen width
    CircleBot.width(18)
    # call turtle.begin_fill() before drawing the circle
    CircleBot.begin_fill()
    # draw the circle
    CircleBot.circle(50)
    # call turtle.end_fill() after drawing the circle
    CircleBot.color('Red')
    CircleBot.end_fill()
    CircleBot.color(Color)
    CircleBot.width(20)
    CircleBot.goto(X,Y+45)
    CircleBot.begin_fill()
    # draw the circle
    CircleBot.circle(5)
    # call turtle.end_fill() after drawing the circle
    CircleBot.end_fill()
    CircleBot.goto(X,100+Y)
    CircleBot.goto(X,50+Y)
    CircleBot.goto(X+50,Y+50)
    CircleBot.goto(X,Y+50)
    CircleBot.goto(-50+X,50+Y)
    # hide the turtle
    CircleBot.hideturtle()
CircleBot.hideturtle()
# end the program
done()
