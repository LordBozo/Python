# circle.py
# set up the program
# import turtle drawing routines
from turtle import *
setup()
x=0
cursor = Turtle()
# end the program
while True:
    x = x+1
    from ctypes import windll, Structure, c_ulong, byref
    class POINT(Structure):
        _fields_ = [("x", c_ulong), ("y", c_ulong)]
    def queryMousePosition():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return { "x": pt.x-970, "y": pt.y- 580}
    pos = queryMousePosition()
    title(pos)
    cursor.goto(x,1)
done()
