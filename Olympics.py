from turtle import *# import turtle drawing routines
setup()#steup the drawing window
title("Olympic Rings")# create a title for the drawing window
turtle = Turtle()# create a turtle to draw with
while True: #cuz why not
    turtle.up()# lift the pen up (away from the window)
    turtle.goto(0,0)# set the starting point for the drawing pen.
    title("Olympic Rings: Black")#change title to current color
    turtle.down()# put the pen down (against the window)
    turtle.width(10)# set the pen width
    turtle.color('Black')# set the pen color
    turtle.circle(70) #draw the circle
    turtle.up() #Move up to move to the next area
    turtle.goto(105,0) #set the starting point for the drawing pen.
    title("Olympic Rings: Red")#change title to current color
    turtle.down()# put the pen down (against the window)
    turtle.color('Red')# set the pen color
    turtle.width(10)# set the pen width
    turtle.circle(70)# draw the circle
    turtle.up()#Move up to move to the next area
    turtle.goto(-105,0)# set the starting point for the drawing pen.
    title("Olympic Rings: Blue")#change title to current color
    turtle.down()# put the pen down (against the window)
    turtle.color('Blue')# set the pen color
    turtle.width(10)# set the pen width
    turtle.circle(70)# draw the circle
    turtle.up()#Move up to move to the next area
    turtle.goto(55,-80)# set the starting point for the drawing pen.
    title("Olympic Rings: Green")#change title to current color
    turtle.down()# put the pen down (against the window)
    turtle.color('Lime Green')# set the pen color
    turtle.width(10)# set the pen width
    turtle.circle(70)# draw the circle
    turtle.up()#Move up to move to the next area
    turtle.goto(-55,-80)# set the starting point for the drawing pen.
    title("Olympic Rings: Yellow")#change title to current color
    turtle.down()# put the pen down (against the window)
    turtle.color('Yellow')# set the pen color
    turtle.width(10)# set the pen width
    turtle.circle(70)# draw the circle
    turtle.hideturtle()#Hide the turtle
title("Olympic Rings: Finished")#change title to current color
done()# end the program
