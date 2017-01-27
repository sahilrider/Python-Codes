'''A four iteration Snowflake Koch Curve'''

import turtle

def draw_koch_curve(t,n):
    if n<3:
        t.fd(n)
        return
    else:
        draw_koch_curve(t,n//3)
        t.lt(60)
        draw_koch_curve(t,n//3)
        t.rt(120)
        draw_koch_curve(t,n//3)
        t.lt(60)
        draw_koch_curve(t,n//3)

def snowflake(t,n):
    '''Draws snowflake on a Triangle'''
    for i in range(3):
        draw_koch_curve(t,n)
        t.rt(120)

#test run

bob=turtle.Turtle()

'''Shifting Pointer'''
bob.pu()
bob.bk(150)
bob.pd()
'''Shifting complete'''

snowflake(bob,300)
turtlr.mainloop()
