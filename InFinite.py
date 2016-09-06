#Infinte
from turtle import *
setup()
FiniteR = Turtle()
FiniteB = Turtle()
FiniteR.color('Red')
FiniteB.color('Black')
x = 0
while True:
    x = x + 2
    FiniteR.circle(x)
    FiniteB.circle(x+1)
