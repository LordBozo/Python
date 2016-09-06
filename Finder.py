# circle.py
# set up the program
# import turtle drawing routines
from turtle import *
setup()
x=0
cursor = Turtle()
while True:
    x = x+1
    from ctypes import windll, Structure, c_ulong, byref #more setup stuff, importing functions
    class POINT(Structure):
        _fields_ = [("x", c_ulong), ("y", c_ulong)]
    def queryMousePosition():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return { "x": (pt.x - 960), "y": (pt.y - 540) * -1}
    pos = queryMousePosition()
    title(pos)
    cursor.goto(x , 500)
done()
