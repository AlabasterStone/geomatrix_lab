from sympy import *

x_,y_ = symbols("x y")

class GeoMatrix():
    def __init__(self) -> None:
        self.points = dict()

    def addPoint(self, symbol, x, y):
        self.points[symbol] = (x,y)
    
    def extend(self, a, b, symbol):
        x = b[0]+b[0]-a[0]
        y = b[1]+b[1]-a[1]
        self.addPoint(symbol, x, y)
        return x, y

    def perpandicularLine(self, k, x, y):
        b_ = symbols("b")
        kx = -(1/k)
        #bx = (sqrt(pow(x,2)+pow(y,2))/k)*sqrt(1+pow(k,2))
        bx = solve(kx*x+b_-y,b_)
        return Eq(kx*x_+bx-y_,0)
    
    def bisectorLine(self,a1,b1,c1, a2,b2,c2,angle):
        if angle:
            return Eq(((a1*x_+b1*y_+c1)/sqrt(a1**2+b1**2))+((a2*x_+b2*y_+c2)/sqrt(a2**2+b2**2)),0)
        else:
            return Eq(((a1*x_+b1*y_+c1)/sqrt(a1**2+b1**2))-((a2*x_+b2*y_+c2)/sqrt(a2**2+b2**2)),0)


axis = GeoMatrix()
y1 = 2*x_
y2 = axis.perpandicularLine(2,2,4)
plot(y1,y2,x_)