import numpy as np
import matplotlib.pyplot as plt

dx = 0.01  
dt = 0.001  
L = 1.0
dam =0

s = dt /(2* dx**2)

m1 = 1    # slope for length of 0 to 0.1
m2 = -1/9  # slope for length of 0.1 - 1

u_now = [m1*i*dx for i in range (0,11)]+[(m2*i*dx)-m2 for i in range (11,101)]

u_prev = u_now.copy()
u_next = [0 for i in range (0,101)]

x = [i*0.01 for i in range (0,101)]

plt.figure()
for i in range(10000000):
    for j in range(1, 100):
        f =(dx**2*dam*(u_prev[j]))  # good
        f2= 2*dt*(u_now[j + 1] - 2 * u_now[j] + u_now[j - 1]) # good
        f3= (2 * u_now[j] - u_prev[j]) #good
        u = s * (-f+f2)+ f3 
        u_next[j] = u - (dam*u*dt)

    u_prev = u_now[:]
    u_now = u_next[:]
    if i%100 == 0:
        
        plt.clf()
        plt.plot(x,u_now)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.4, 0.4)
        plt.pause(0.001)


##    u_next[0] = 0
##    u_next[-1] = 0                   
##    u_prev[:] = u_now  
##    u_now[:] = u_next 
##        
##    if i % 50 == 1:

##plt.show()
