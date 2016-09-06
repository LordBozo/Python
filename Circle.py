# circle.py
# set up the program
# import turtle drawing routines
from turtle import *
# create the drawing window
setup()
# create a title for the drawing window
title("circle program")
# create a turtle to draw with
turtle = Turtle()
Color = 'Red'
# draw the circle
# lift the pen up (away from the window)
# so it doesn't draw a line as it moves
turtle.up()
# set the starting point for the drawing pen.
turtle.goto(0,0)
# put the pen down (against the window) 
# so it can begin to draw
turtle.down()
# set the pen color
turtle.color(Color)
# set the pen width
turtle.width(10)
# call turtle.begin_fill() before drawing the circle
turtle.begin_fill()
# call turtle.end_fill() after drawing the circle
turtle.end_fill()
# hide the turtle
turtle.color('Red')
# set the pen width
turtle.width(10)
# call turtle.begin_fill() before drawing the circle
turtle.begin_fill()
# draw the circle
turtle.circle(40)
# call turtle.end_fill() after drawing the circle
turtle.end_fill()
#
##2
#
turtle.up()
# set the starting point for the drawing pen.
turtle.goto(0,15)
# put the pen down (against the window) 
# so it can begin to draw
turtle.down()
# set the pen color
turtle.color('Blue')
# set the pen width
turtle.width(10)
# call turtle.begin_fill() before drawing the circle
turtle.begin_fill()
# draw the circle
turtle.circle(25)
# call turtle.end_fill() after drawing the circle
turtle.end_fill()
# hide the turtle
turtle.color(Color)
# set the pen width
turtle.width(10)
# call turtle.begin_fill() before drawing the circle
turtle.begin_fill()
# call turtle.end_fill() after drawing the circle
turtle.end_fill()
turtle.up()
# set the starting point for the drawing pen.
turtle.goto(0,30)
# put the pen down (against the window) 
# so it can begin to draw
turtle.down()
# set the pen color
turtle.color(Color)
# set the pen width
turtle.width(10)
# call turtle.begin_fill() before drawing the circle
turtle.begin_fill()
# call turtle.end_fill() after drawing the circle
turtle.end_fill()
# hide the turtle
turtle.color('Lime Green')
# set the pen width
turtle.width(10)
# call turtle.begin_fill() before drawing the circle
turtle.begin_fill()
# draw the circle
turtle.circle(10)
# call turtle.end_fill() after drawing the circle
turtle.end_fill()
turtle.hideturtle()
title("Finished")
# end the program
done()
