from hwx import *
import os 

a = ""
m = ""

def num(n):
    global a
    a += str(n)
    display.set(a)

def clear():
    global a, m
    a = ""
    m = ""
    display.set("")

def add():
    global a, m
    m = a + "+"
    a = ""
    display.set(m)

def sub():
    global a, m
    m = a + "-"
    a = ""
    display.set(m)

def mul():
    global a, m
    m = a + "*"
    a = ""
    display.set(m)

def div():
    global a, m
    m = a + "/"
    a = ""
    display.set(m)

def equ():
    global a, m
    m += a
    try:
        result = str(eval(m))
        display.set(result)
        a = result  # Store result for further calculations
    except:
        display.set("Error")
        a = ""
        m = ""

display = gui.TextBox(text="", width=20, readonly=True)

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

    gui.PushButton("C", command=clear),
    gui.PushButton("0", command=lambda: num(0)),
    gui.PushButton("=", command=equ),
    gui.PushButton("/", command=div),
), nrows=4, border=5, spacing=5)


show(button_grid)
