from matplotlib.figure import Figure
import matplotlib.pyplot as plt

dx = 0.1
dt = 0.01

u_time = []
u_pos = []




for i in range(10000000):
    
    
 
    if(i%50 == 1):
    #if True:
        plt.clf()
        plt.plot(extent, unext)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-1.0, 1.0)
        plt.pause(0.001)
plt.show()