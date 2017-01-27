import turtle
import math

def square(t,l):
    for i in range(4):
        t.fd(l)
        t.lt(90)

def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,n,length):
    angle=360/n
    polyline(t,n,length,angle)

def arc(t,r,angle):
    arc_length=2*math.pi*r*abs(angle)/360
    n=int(arc_length/4)+1
    l=arc_length/n
    step_angle=float(angle)/n

    t.lt(step_angle/2)
    polyline(t,n,l,step_angle)
    t.rt(step_angle/2)

def circle(t,r):
    #to print circle centered on origin next 4 lines are written
    #pen up means nothing in printed or movement of pen without printing anything
    #pen down means now it is ready to print
    t.pu()  #pen up
    t.fd(r)
    t.lt(90)
    t.pd()  #pen down
    arc(t,r,360)

#Running test program

bob=turtle.Turtle()
#square(bob,100)
#polygon(bob,10,100)

circle(bob,100)
#arc(bob,100,60)

turtle.mainloop()

