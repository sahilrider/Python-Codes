import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

bob=turtle.Turtle()
bob.lt(90)
draw(bob,10,5)
bob.lt(180)
draw(bob,10,5)
bob.mainloop()
