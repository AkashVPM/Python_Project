from hwx import gui
from hwx.gui.XyPlot import XyPlot

icon="dialogOptimizationDesignSpacePercentStrip-48.png"

plot = XyPlot(title="Game", size=(10, 5))

plot.xlimits = (0, 4.0)
plot.ylimits = (0, 1.0)

x = [1,2]
y = [0.4, 0.6]

plot.addCurve(x=x, y=y, fit=False, draggable=False, color = Green)

gui.show(plot)
