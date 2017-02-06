'''To check if a point or rectangle lies in/on circle'''

import math

class Point:
    '''Represents a point in 2D
       Atrributes: x,y'''

class Rectangle:
    '''Represents a rectangle.
       Attributes: C1 and C2 of primary diagonal'''

class Circle:
    '''Represents a Circle.
       Attributes: Center and radius'''

def distance(p1,p2):
    res=math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
    return res

def point_in_circle(p,c):
    '''p:point , c:circle'''
    if distance(p,c.center)<=c.radius:
        return True
    else:
        return False

def rect_in_circle(rect,c):
    if distance(rect.c1,c.center)>c.radius:
        return False
    if distance(rect.c2,c.center)>c.radius:
        return False
    return True

def main():
    rect=Rectangle()
    rect.c1=Point()
    rect.c2=Point()
    rect.c1.x=-3
    rect.c1.y=1
    rect.c2.x=3
    rect.c2.y=-1

    circle=Circle()
    circle.center=Point()
    circle.center.x=0
    circle.center.y=0
    circle.radius=5
    
    print(point_in_circle(rect.c1,circle))
    print(point_in_circle(rect.c2,circle))
    print(rect_in_circle(rect,circle))
    
if __name__=='__main__':
    main()
