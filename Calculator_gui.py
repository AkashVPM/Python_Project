from hwx import *
import os 

a = ""
def num(n):
    global a
    a += str(n)
    gui.tellUser(a)
def add (): 
    global a 
    a += "+"
    gui.tellUser(a)
def sub (): 
    global a 
    a += "-"
    gui.tellUser(a)
def mul (): 
    global a 
    a += "*"
    gui.tellUser(a)
def equ (): 
    global a 
    a = str(eval(a))
    gui.tellUser(a)
def div (): 
    global a 
    a += "/"
    gui.tellUser(a)
def flo ():
    global a 
    a += "."
    gui.tellUser(a)
def clear ():
    global a 
    a = ""
    gui.tellUser(a)
def open_bracket ():
    global a 
    a += "("
    gui.tellUser(a)
def close_bracket ():
    global a 
    a += ")"
    gui.tellUser(a)
def deleted ():
    global a 
    a = a[:-1]
    gui.tellUser(a)
    
button_grid = gui.GridFrame((
    gui.PushButton("1", command=lambda: num(1)),
    gui.PushButton("2", command=lambda: num(2)),
    gui.PushButton("3", command=lambda: num(3)),
    gui.PushButton("+", command=add),
    
    gui.PushButton("4", command=lambda: num(4)),
    gui.PushButton("5", command=lambda: num(5)),
    gui.PushButton("6", command=lambda: num(6)),
    gui.PushButton("-", command=sub),

    gui.PushButton("7", command=lambda: num(7)),
    gui.PushButton("8", command=lambda: num(8)),
    gui.PushButton("9", command=lambda: num(9)),
    gui.PushButton("*", command=mul),

    gui.PushButton("dot", command=flo),
    gui.PushButton("0", command=lambda: num(0)),
    gui.PushButton("=", command=equ),
    gui.PushButton("/", command=div),

    gui.PushButton("c", command=clear),
    gui.PushButton("(", command=open_bracket),
    gui.PushButton(")", command=close_bracket),
    gui.PushButton("del", command=deleted),
), nrows=4, border=5, spacing=5)

show(button_grid)
