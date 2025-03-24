from hwx import gui
from hwx.gui.XyPlot import XyPlot
import random 

number = [ i for i in range (10)] 
toss = random.choice(number)
print (toss)

upper_index = [gui.Button() for i in range (10)]
last_index =[gui.Button() for i in range (10)] 
last_index [1] = gui.Button(icon="msobjbrowser.png",)
if toss % 3 == 0:
      last_index [-1] = gui.Button(icon= "glyphDeleteStrip-16.png",)


layout = gui.VFrame(
      gui.HFrame (upper_index),
      gui.HFrame (last_index), border = 100, spacing = 10, margin = 50)

gui.show (layout)