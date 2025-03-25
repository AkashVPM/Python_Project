from hwx import gui
from hwx.gui.XyPlot import XyPlot
import random 
gui.addresource path ("file title)

# random function to create obstacle 
number = [ i for i in range (10)] 
toss = random.choice(number)
print (toss)

# Buttons layout
upper_index = [gui.Button() for i in range (10)]
last_index =[gui.Button() for i in range (10)] 
last_index [1] = gui.Button(icon="msobjbrowser.png",)

#obstacle creation for game
if toss % 3 == 0:
      last_index [-1] = gui.Button(icon= "glyphDeleteStrip-16.png",)

# make time function to move the boxeS

# move_box = last_index [1:] +last_index [:1]
# for i in range (1000):
#       x = inspire.time(500)
#       x.connect (move_box)

layout = gui.VFrame(
      gui.HFrame (upper_index),
      gui.HFrame (last_index), border = 100, spacing = 10, margin = 50)

gui.show (layout)
