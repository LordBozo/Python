# star
from turtle import *
setup()
Staryu = Turtle()
Staryu1 = Turtle()
Staryu2 = Turtle()
x = 0
Staryu2.up()
Staryu2.goto(-40,0)
Staryu2.down()
Staryu2.color('Red')
Staryu1.up()
Staryu1.goto(0,2)
Staryu1.down()
Staryu1.color('Black')
Staryu.up()
Staryu.goto(60,5)
Staryu.down()
Staryu.color('Red')
while (x != 72):
    x = x + 1
    Staryu.left(12)
    Staryu.forward(50)
    Staryu.left(168)
    Staryu.forward(50)
    Staryu.right(175)
    if (x<37):
        Staryu1.left(12)
        Staryu1.forward(50)
        Staryu1.left(168)
        Staryu1.forward(50)
        Staryu1.right(170)
    if(x<19):
        Staryu2.left(12)
        Staryu2.forward(40)
        Staryu2.left(168)
        Staryu2.forward(40)
        Staryu2.right(160)
Staryu.hideturtle()
Staryu1.hideturtle()
Staryu2.hideturtle()


