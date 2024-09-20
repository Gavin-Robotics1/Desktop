import math

class Ball:

    def __init__(self,mass,radius,pos,vel,force,dragC):

        self.pos=pos
        self.mass=mass
        self.vel=vel
        self.acc=force/mass
        self.force=force
        self.C=dragC
        self.A=math.pi*radius**2