import Rectangle_area

def tri_area(a,b,c):  
        point = a,b,c
        [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]] = point
        a = ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5
        b = ((x1-x3)**2+(y1-y3)**2+(z1-z3)**2)**0.5
        c = ((x3-x2)**2+(y3-y2)**2+(z3-z2)**2)**0.5
      
      # Find the area of Actuator body using Heron's Formula
        s = (a+b+c)/2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area
 
def quard_point (*args):
        check = list (args)
        for i in range (4):
                a,b,c,d = check 
                area_1 = tri_area(a,b,c)
                area_2 = tri_area(a,c,d)
                area_3 = tri_area(a,b,d)
                area_4 = tri_area(b,c,d)
                if abs(area_1 - (area_2 + area_3 + area_4) ) <= 10e-14:
                        print("concave")
                        break
                else:
                        print("convex")
                        check = check[3:] + check[:3]
        print (check)
        fun = Rectangle_area.rectangle(*check)
        Rectangle_area.write_1 (fun)
             
quard_point ([0.5,0.5,0],[1,0,0],[0,0,0],[0,1,0] )