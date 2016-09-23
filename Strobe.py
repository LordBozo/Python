from tkinter import *
import time
import random

WIDTH = 1920
HEIGHT = 1024

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("Drawing")
canvas.pack()
NUMX= -1
NUMY = 0
NumYEnd = 10
NumXEnd = 10
NUM = 3

colors = ['red', 'green', 'blue', 'orange', 'orange', 'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'yellow', 'red', 'pink']

class Q1:
    def __init__(self):
        self.shape = canvas.create_rectangle((NUMX/NumXEnd)*WIDTH, HEIGHT*(NUMY/NumYEnd), ((NUMX+1)/NumXEnd)*WIDTH, HEIGHT*((NUMY+1)/NumYEnd), fill=random.choice(colors) )

    def update(self):
        self.shape = canvas.create_rectangle((NUMX/NumXEnd)*WIDTH, HEIGHT*(NUMY/NumYEnd), ((NUMX+1)/NumXEnd)*WIDTH, HEIGHT*((NUMY+1)/NumYEnd), fill=random.choice(colors) )




ball_list = []
for ITERABLEX in ((str)(WIDTH/NumXEnd)):
    NUMX=NUMX+1
    NUMY= 0
    for ITERABLEY in ((str)(HEIGHT/NumYEnd)):
        NUMY=NUMY+1
        ball_list.append(Q1())
NUMX = -1
NUMY=3
while True:
    for ITERABLEX in ((str)(WIDTH/NumXEnd)):
        NUMX=NUMX+1
        NUMY= -2
        for ITERABLEY in ((str)(HEIGHT/NumYEnd)):
            NUMY=NUMY+1
            Q1.update(Q1())
            tk.update()
    NUMX=-1
    NUMY=3
    
    time.sleep(.01)
