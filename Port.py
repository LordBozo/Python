#Infinte
from turtle import *
import math
import turtle
setup()
Shapes = Turtle()
while True:
    Shapes.up()
    OffsetX = int( input("X Starting Point: "))# Input any Integer with int()
    OffsetY = int( input("Y Starting Point: "))# Input any Integer with int()
    Shapes.goto(OffsetX, OffsetY)
    Shapes.down()
    Color = input("Color: ") # accepts an input
    Shapes.color(Color)
    BG = input("Background Color: ")
    bgcolor(BG)
    Width = int(input("Width: "))# Input any Integer with int()
    Sides = int(input("Sides: "))# Input any Integer with int()
    Radius = int(input("Side Length: "))# Input any Integer with int()
    #Setup for drawing
    X = 0
    Shapes.degrees()
    Shapes.up()
    Shapes.down()
    Shapes.color(Color)
    Shapes.width(Width)
    while (X <= (Sides - 1)):
        X = X + 1
        Shapes.forward(Radius)# Draws the polygon
        Shapes.left(360/Sides)
