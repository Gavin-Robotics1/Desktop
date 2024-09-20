#physics goes here

import ball

t=0
dt=0.01
g=9.8

ball=ball.Ball(10,0.1,100,0,-98,0.5)

def move(a):
    a.acc=a.force/a.mass
    a.pos+=a.vel*dt
    a.vel+=a.acc*dt
    if a.pos<=-300:
        print(a.vel)
        a.vel=0
        run=False