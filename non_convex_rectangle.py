import random

def triangle (a,b,c):
    while True:
        r1 = random.random()
        r2 = (1-r1)*random.random()
        r3 = 1-r1-r2
        if r1 + r2 + r3  == 1 :
            
            p = a,b,c 
            [x1,y1,z1], [x2,y2,z2], [x3,y3,z3] = p 
            #print (p)

            point_1 =  r1*x1 + r2*x2 + r3*x3
            point_2 =  r1*y1 + r2*y2 + r3*y3
            point_3 =  r1*z1 + r2*z2 + r3*z3

            yield [point_1,point_2,point_3]

Po = [1,0,0],[0,1,0],[1,1,0], [0,0,0]   
fun_1 = triangle (Po[0],Po[1],Po[2])
fun_2 = triangle (Po[0],Po[2],Po[3])


with open ("C:/Akash S/Rectangle_poins.csv","w") as f :
    for i in range (10000):
        p = next(fun_1)
        q = next(fun_2)
        f.write(str(p[0])+ ',' +str(p[1])+ ','+
         str(q[0])+ ',' +str(q[1])+ ','+str(p[2]) + ','+str(q[2])+'\n')