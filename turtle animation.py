import turtle
colors=['red','purple','blue','green','orange','yellow']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)


'''
/*wn = turtle.Screen()
skk = turtle.Turtle()
skk.color("blue")
skk.speed(9)
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size=size-5

sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
'''

