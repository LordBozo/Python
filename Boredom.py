from turtle import *
import time
import random
from tkinter import *
setup()
Wi = 10
title('Squares')
Square = Turtle()
colors = ['red', 'green', 'blue', 'orange',  'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'yellow', 'red', 'pink']
Square.up()
Square.goto(-(1900/2),510)
Square.down()
Square.speed('fastest')
bgcolor('black')
for Z in range((int)(1900/Wi)):
    for b in range((int)(1020/Wi)):
        Square.color(random.choice(colors))
        Square.begin_fill()
        bgcolor(random.choice(colors))
        for i in range(4):
            Square.forward(Wi)
            bgcolor(random.choice(colors))
            Square.right(90)
            bgcolor(random.choice(colors))
        Square.end_fill()
        Square.left(90)
        Square.back(Wi)
        Square.right(90)
        bgcolor(random.choice(colors))
    Square.up()
    Square.forward(Wi)
    Square.left(90)
    Square.forward((int)(1020/Wi)*Wi)
    Square.right(90)
    Square.down()
