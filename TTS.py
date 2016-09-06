from turtle import * #grab turtle methods
import random # grab random stuff
setup() # create drawing window
turtle = Turtle() # defines turtle
while True:
    Text = input("Text: ") # set Text as a string
    title("Text To Turtle") # names drawing window
    for x in range(0, len(Text)): # Loop through text
        XY = int(random.randrange(10,35)) # create random font size
        turtle.write(Text[x:x+1] + " ", font = ("Arial", XY, "normal")) # draw letters
        turtle.forward(.9 * XY) # move turtle forward
