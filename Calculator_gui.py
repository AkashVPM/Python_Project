from hwx import *
import os 
a = 0
m = 1

def num_1 (): return 1
def num_2 (): return 2
def num_3 (): return 3
def num_4 (): return 4
def num_5 (): return 5
def num_6 (): return 6
def num_7 (): return 7
def num_8 (): return 8
def num_9 (): return 9
def num_0 (): return 0
def flo (*a): return float(*a)
def equ (): return stop 
def add (*a): return (a + num)
def sub (*a): return (a - num)
def mul (*a): return (m * num)
def div (*a): return (m / num)

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

