from hwx import gui
from hwx.gui.XyPlot import XyPlot
import time

plot = XyPlot(title="Game", size=(10, 5))


plot.xlimits = (0, 4.0)
plot.ylimits = (0, 1.0)
x = [i for i in range (10)]
y = [0.2 for i in range (10)]
for i in range (1,10):
      j = i+1
      x = x[i]+x[j]
      y = y[i]+y[j]
      plot.addCurve(x=x, y=y, fit=False, draggable=False, color = "green")
      # x = x[0:0]
gui.show(plot)
