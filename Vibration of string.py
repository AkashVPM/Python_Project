import numpy as np
import matplotlib.pyplot as plt

dx = 0.01  
dt = 0.0005  
L = 1.0  

u_time = np.zeros((0, 3))  
extent = np.linspace(0, L)

N = int(1/0.01)

plt.figure()
for i in range(10000000):
    for j in range(1,N):
        u_time[j, 2] = ((u_time[j + 1, 1] - 2 * u_time[j, 1] + u_time[j - 1, 1]) * dt ** 2 / dx ** 2) + 2 * u_time[j, 1] - u_time[j, 0]
    
    u_time[0, 2] = 0
    u_time[-1, 2] = 0
    
    u_time[:, 0], u_time[:, 1] = u_time[:, 1], u_time[:, 2]

    if i % 50 == 1:
        plt.clf()
        plt.plot(extent, u_time[:, 1])
        plt.xlim(-0.1, 1.1)
        plt.ylim(-1.0, 1.0)
        plt.pause(0.001)

plt.show()
