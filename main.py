from math import *

def distance(a,b):
    return sqrt(pow((b[0]-a[0]),2)+pow((b[1]-a[1]),2))

def extend(a,b):
    x = b[0]+b[0]-a[0]
    y = b[1]+b[1]-a[1]
    return (x,y)

C = (0,0)
B = (-2,0)
A = (distance(B,C)/2,distance(B,C)/2)
E = extend(B,C)
BD = distance(B,C)-distance(A,B)
CBD = 45
Dx = BD/sin(90-CBD)
Dy = BD/cos(90-CBD)
D = (Dx,Dy)
F = extend(D,C)