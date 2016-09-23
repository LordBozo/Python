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

