from ctypes import *
from tkinter import *
import time
import random

WIDTH = 1920
HEIGHT = 1024

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("Drawing")
canvas.pack()

colors = ['red', 'green', 'blue', 'orange', 'orange', 'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'yellow', 'red', 'pink']
x=0

class Ball:
    def __init__(self):
        self.size = random.randrange(200, 400)
        offsetx = random.randrange(1,1500)
        offsety = random.randrange(1,600)
        color = random.choice(colors)
        self.shape = canvas.create_oval(offsetx , offsety, offsetx + self.size, offsety + self.size, fill=color, )
        self.speedx = random.randrange(10, 100)
        self.speedy = random.randrange(10, 100)

    def update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1
ball_list = []
for i in range(1):
    ball_list.append(Ball())
while True:
    for ball in ball_list:
        ball.update()
    x = x+1
    class POINT(Structure):
        _fields_ = [("x",c_ulong), ("y",c_ulong)]
    def queryMousePosition():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return { "x": (pt.x - 960), "y": (pt.y - 540) * -1}
    pos = queryMousePosition()

