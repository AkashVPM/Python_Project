import numpy as np
import matplotlib.pyplot as plt

dx = 0.01  
dt = 0.001  
L = 1.0
dam =1

s = dt**2 /(dx**2)

m1 = 1    # slope for length of 0 to 0.1
m2 = -1/9  # slope for length of 0.1 - 1

u_now = [m1*i*dx for i in range (0,11)]+[(m2*i*dx)-m2 for i in range (11,101)]

u_prev = u_now.copy()
u_next = [0 for i in range (0,101)]

x = [i*0.01 for i in range (0,101)]

plt.figure()
for j in range(10000000):
    for i in range(1, 100):
        f = 2*dt/(2*dt-dam*dt**2)
        f1 = (u_now[i + 1] - 2 * u_now[i] + u_now[i - 1])
        f2 = dam * dt**2 * u_prev[i]*0.5/dt
        f3 = 2 * u_now[i] - u_prev[i]
        u = f * ((s*f1) - f2 + f3)
        u_next[i] = u

##        f =(dx**2*dam*(u_prev[j]))  # good
##        f2= 2*dt*(u_now[j + 1] - 2 * u_now[j] + u_now[j - 1]) # good
##        f3= (2 * u_now[j] - u_prev[j]) #good
##        u = (s * (-f+f2))+f3 
##        u_next[j] = u - (dam*u*dt/2)

    u_prev = u_now[:]
    u_now = u_next[:]
    if j%50 == 0:
        
        plt.clf()
        plt.plot(x,u_now)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.4, 0.4)
        plt.pause(0.001)
plt.show()



import numpy as np
import matplotlib.pyplot as plt

dx = 0.01  
dt = 0.001  
L = 1.0
dam =1

s = dt**2 /(dx**2)

m1 = 1    # slope for length of 0 to 0.1
m2 = -1/9  # slope for length of 0.1 - 1

u_now = [m1*i*dx for i in range (0,11)]+[(m2*i*dx)-m2 for i in range (11,101)]

u_prev = u_now.copy()
u_next = [0 for i in range (0,101)]

x = [i*0.01 for i in range (0,101)]

plt.figure()
for j in range(10000000):
    for i in range(1, 100):
        f = 2*dt/(2*dt-dam*dt**2)
        f1 = (u_now[i + 1] - 2 * u_now[i] + u_now[i - 1])
        f2 = dam * dt**2 * u_prev[i]*0.5/dt
        f3 = 2 * u_now[i] - u_prev[i]
        u = f * ((s*f1) - f2 + f3)
        u_next[i] = u

##        f =(dx**2*dam*(u_prev[j]))  # good
##        f2= 2*dt*(u_now[j + 1] - 2 * u_now[j] + u_now[j - 1]) # good
##        f3= (2 * u_now[j] - u_prev[j]) #good
##        u = (s * (-f+f2))+f3 
##        u_next[j] = u - (dam*u*dt/2)

    u_prev = u_now[:]
    u_now = u_next[:]
    if j%50 == 0:
        
        plt.clf()
        plt.plot(x,u_now)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.4, 0.4)
        plt.pause(0.001)
plt.show()



