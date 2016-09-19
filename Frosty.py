from turtle import *
import time
import random
setup()
title('Snowman')
R1 = 40 #radius
Loop = 4 #number of balls
Per = 1.4 #percent decrease
Wi = 10 #width
Ti = 10 #tilt
Snowman = Turtle() #define the turtle
Snowman.width(Wi) #specify the width of the turtle's pen
Snowman.up()
Snowman.left(90)
Snowman.back(460)
Snowman.right(90)
Snowman.down()
for i in range(Loop): # start a loop for the base
    R1 = Per * R1
    Snowman.speed("fastest")
    Snowman.begin_fill()
    Snowman.forward(R1/5)
    Snowman.left(10)
    Snowman.circle(R1,170)
    Snowman.forward(R1/2.5)
    Snowman.left(10)
    Snowman.circle(R1,170)
    Snowman.forward(R1/5)
    Snowman.left(90)
    Snowman.color('White')
    Snowman.end_fill()
    Snowman.color('Black')
    Snowman.up()
    Snowman.forward((2*R1)-1)
    if (i != 0) & (i != (Loop - 1 )):   #on the second ball
        Snowman.back((2*R1)-1)   #go back
        for a in range(3):
            Snowman.forward(.5*R1)   #draw the circles
            Snowman.down()
            Snowman.circle(1)
            Snowman.up()
        Snowman.forward(.5*R1) #go to the top of the current ball
    Snowman.down()
    Snowman.right(90+Ti) #finish
Snowman.up()
Snowman.width(Wi/2)
Snowman.right(70.71-Ti)
Snowman.forward(R1*1.0594)   #move into position for the eyes
Snowman.left(70.71)
for i in range(2):
    Snowman.down()
    Snowman.begin_fill()
    Snowman.circle(.125 * R1)   # draw the eyes
    Snowman.end_fill()
    Snowman.up()
    Snowman.back(.8 * R1)
Snowman.right(22.61986495)  #move to draw mouth
Snowman.forward(1.3 * R1)
Snowman.left(22.61986495)
Snowman.left(90)
Snowman.forward((.2 * R1) - 5)
Snowman.down()
Snowman.forward(5)
Snowman.up()
Snowman.back(.2 * R1)
Snowman.down()
Snowman.right(90)
Snowman.color('Purple')
Snowman.circle(.2 * R1,90)  #draw mouth
Snowman.left(90)
Snowman.forward(.4 * R1)
Snowman.left(90)
Snowman.circle(.2*R1,90)
Snowman.left(55)
Snowman.up()
Snowman.forward(1.7*R1)
Snowman.left(125)
Snowman.down()
Snowman.color('Black')
Snowman.width(2*Wi)
Snowman.forward(2*R1) #start hat
Snowman.back(.5*R1)
Snowman.right(90)
Snowman.begin_fill()
for s in range(2):
    Snowman.forward(1*R1)
    Snowman.right(90)
    Snowman.forward(1*R1)
    Snowman.right(90)
Snowman.end_fill() #finish hat
