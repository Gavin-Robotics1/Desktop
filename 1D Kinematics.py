
import math
import sys
import os

#car starting at v = 0, a = 2, how far after 10 s?

#total distance = 100 m


time = 0
pos = -10
vel = 4.5
#acc = -9.8
acc = 2.5
dt = 1 #step

run = True
while run:
    #position = original position + displacement
    #vel * dt = displacement - fuzzyness
    #vel = vel + deltaV
    #deltaV = acc * dt
    vel += acc*dt
    pos += vel*dt
    time += dt

    if pos < 0:
        os.system("clear")
        print("position ",pos," m ", "time ", time, " s")
        run=False


sys.exit()