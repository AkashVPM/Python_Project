# Author : Akash S
# Barycentric_method : https://en.wikipedia.org/wiki/Barycentric_coordinate_system 

import random

def triangle (a,b,c):
      r1,r2,r3 = random.random(), random.random(), random.random()
      if r1 + r2 + r3  == 1 :
            r1 = 1-r2-r3
            r2 = 1-r3-r1
            r3 = 1-r2-r1
      p = a,b,c 
      [x1,y1,z1], [x2,y2,z2], [x3,y3,z3] = p 
      print (p)

      point_1 = [ r1*x1 + r2*x2 + r3*x3]
      point_2 = [ r1*y1 + r2*y2 + r3*y3]
      point_3 = [ r1*z1 + r2*z2 + r3*z3]

      yield (point_1,point_2,point_3)
          
fun = triangle ([1,0,0],[0,1,0],[0,0,1])
print (next(fun))

     
