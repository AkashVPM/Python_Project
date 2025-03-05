import numpy as np
import pandas as pd

from stl import mesh

# import the STL file 
Actuator_body = mesh.Mesh.from_file(r"Actuator_Body.stl") 

# Find area for all triangles 
area = Actuator_body.areas

# Sum of all triangles 
Total_area = sum(area)

print (f"The total area of all triangles is {Total_area}")