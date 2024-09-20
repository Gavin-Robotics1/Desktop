#FirstPhysicsEngine

import pygame as pg
import sys
import os

#from physicsengine import*

pg.init()

w=800
h=600

screen=pg.display.set_mode((w,h))
pg.display.set_caption("Name")
clock=pg.time.Clock()
run=True

##
from ball import Ball
ball = Ball(10,0.1,100,0,-98,0.5)

from engine import move
##

while run: #main loop "game loop"
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                run=False

    move(ball)
    clock.tick(60)
    screen.fill((200,225,250))
    pg.draw.rect(screen,(180,255,180),(0,h-100,w,100))
    pg.draw.circle(screen,(0,0,0),(w/2,100-ball.pos),5)
    pg.display.flip()



pg.quit()
sys.exit()