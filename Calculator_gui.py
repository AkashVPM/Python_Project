from hwx import *
from hwx import gui
import os

a = ""
def num(n):
    global a
    a += str(n)
def equ (): 
    global a 
    a = str(eval(a))
def clear ():
    global a 
    a = ""
def deleted ():
    global a 
    a = a[:-1]

button_grid = gui.GridFrame((
    gui.PushButton("1", command=lambda: num(1)),
    gui.PushButton("2", command=lambda: num(2)),
    gui.PushButton("3", command=lambda: num(3)),
    gui.PushButton("+", command=lambda: num("+")),
    
    gui.PushButton("4", command=lambda: num(4)),
    gui.PushButton("5", command=lambda: num(5)),
    gui.PushButton("6", command=lambda: num(6)),
    gui.PushButton("-", command=lambda: num("-")),

    gui.PushButton("7", command=lambda: num(7)),
    gui.PushButton("8", command=lambda: num(8)),
    gui.PushButton("9", command=lambda: num(9)),
    gui.PushButton("*", command=lambda: num("*")),

    gui.PushButton("dot", command=lambda: num(".")),
    gui.PushButton("0", command=lambda: num(0)),
    gui.PushButton("=", command=equ),
    gui.PushButton("/", command=lambda: num("/")),

    gui.PushButton("c", command=clear),
    gui.PushButton("(", command=lambda: num("(")),
    gui.PushButton(")", command=lambda: num(")")),
    gui.PushButton("del", command=deleted),
), nrows=4, border=5, spacing=5)

gui.show(button_grid)
