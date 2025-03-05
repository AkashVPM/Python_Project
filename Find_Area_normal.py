# Find the Actuator Body Area by Akash
import math
total_area = 0

# open file text file
file = open(r"Actuator_Body.stl","r")

# Read each line
Lines = file.readlines()

#find ward vertex and select point
point = []
for line in Lines:
      if "vertex" in line:
            vertex = line.split()
            point.append([float(vertex[1]),float(vertex[2]),float(vertex[3])])
            if len(point) == 3:
                  P1 = math.sqrt((point[1][0] - point[0][0])**2 + (point[1][1] - point[0][1])**2 + (point[1][2] - point[0][2])**2)
                  P2 = math.sqrt((point[2][0] - point[1][0])**2 + (point[2][1] - point[1][1])**2 + (point[2][2] - point[1][2])**2)
                  P3 = math.sqrt((point[0][0] - point[2][0])**2 + (point[0][1] - point[2][1])**2 + (point[0][2] - point[2][2])**2)
 
 # Find the area of Actuator body using Heron's Formula
                  s = (P1+P2+P3)/2
                  area = (s * (s - P1) * (s - P2) * (s - P3))**0.5
                  point = []
                  total_area = total_area + area

# print the total area of actuator body
print (f"The total area of all triangles is {total_area }")



                  
            

            
            



