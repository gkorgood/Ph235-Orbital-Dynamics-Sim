from __future__ import division,print_function
import math as m
from visual import *

##Constants
G = 0.0000000000667408
t = 0
deltat = 0.6

##Earth Constants
earth = sphere(pos=[-75000000,0],radius=6371000,color=(0,0.5,0.5))
earthmass = 5972000000000000000000000

##Second planet constants.
earth2 = sphere(pos=[75000000,0],radius=6371000,color=(0.5,0.5,0.5))
earth2mass = 5972000000000000000000000

##Ship Initial Conditions
ship = sphere(pos=[0,0],radius=5000,color=color.red)
ship.velocity = vector(1500,-2500)##m.sqrt(G * earthmass / ship.pos.x)
earthdist = m.sqrt(m.pow(earth.pos.x-ship.pos.x,2)+m.pow(earth.pos.y-ship.pos.y,2))
earth2dist = m.sqrt(m.pow(earth2.pos.x-ship.pos.x,2)+m.pow(earth2.pos.y-ship.pos.y,2))
veltot = m.sqrt(m.pow(ship.velocity.x,2)+m.pow(ship.velocity.y,2))
##print("v=",ship.velocity)
shipmass = 75000
ship.trail = curve(color=ship.color)

##Energy Check
U = (-G * earthmass * shipmass)/earthdist
earth2U = (-G * earthmass * shipmass)/earth2dist
K = 0.5 * shipmass * (m.pow(veltot,2))
print(U+earth2U+K)
##E = text(text='The energy of the ship is: %f' % (U+K),align='right', pos=(10000,0), height = 2000, depth=0.01, color=color.white)

while t < 1000000:
    rate(10000000)
    
    ##Get the ship's current Location, Velocity, and Energy
    earthdist = m.sqrt(m.pow(earth.pos.x-ship.pos.x,2)+m.pow(earth.pos.y-ship.pos.y,2))
    earth2dist = m.sqrt(m.pow(earth2.pos.x-ship.pos.x,2)+m.pow(earth2.pos.y-ship.pos.y,2))
    veltot = m.sqrt(m.pow(ship.velocity.x,2)+m.pow(ship.velocity.y,2))
    U = (-G * earthmass * shipmass)/earthdist
    earth2U = (-G * earthmass * shipmass)/earth2dist
    K = 0.5 * shipmass * (m.pow(veltot,2))
    ##E.text = 'The energy of the ship is: %f' % (U+K)
    print(U+earth2U+K)
    
    ##Calculate Acceleration
    earthacc = (G * earthmass) / m.pow(earthdist,2)
    earth2acc = (G * earth2mass) / m.pow(earth2dist,2)
    earthaccx = earthacc * ((earth.pos.x-ship.pos.x) / earthdist)
    earthaccy = earthacc * ((earth.pos.y-ship.pos.y) / earthdist)
    earth2accx = earth2acc * ((earth2.pos.x-ship.pos.x) / earth2dist)
    earth2accy = earth2acc * ((earth2.pos.y-ship.pos.y) / earth2dist)
    
    shipaccx = earthaccx + earth2accx
    shipaccy = earthaccy + earth2accy
    
    ##Update Ship's Position
    ship.pos.x = ship.pos.x + (ship.velocity.x * deltat) + (0.5 * (shipaccx) * m.pow(deltat,2))
    ship.pos.y = ship.pos.y + (ship.velocity.y * deltat) + (0.5 * (shipaccy) * m.pow(deltat,2))
    ##print("x=",ship.pos)
    
    ##Update Ship's Velocity
    ##print("v=",ship.velocity)
    ship.velocity.x = ship.velocity.x + shipaccx*deltat
    ship.velocity.y = ship.velocity.y + shipaccy*deltat
    
    ##Leave an Orbit Line
    ship.trail.append(pos=ship.pos)
    
    ##Increment Time
    t = t + deltat