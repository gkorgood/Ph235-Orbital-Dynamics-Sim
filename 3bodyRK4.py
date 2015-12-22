##	Currently Not Functional

from __future__ import division,print_function
import math as m
from visual import *

##Constants
G = 0.0000000000667408
t = 0
deltat = 0.06

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
    rate(10)
    
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
    
    ##Update Ship's Position, Velocity
    k1 = ship.pos.x + (ship.velocity.x * deltat) + (0.5 * (shipaccx) * m.pow(deltat,2))
    l1 = ship.pos.y + (ship.velocity.y * deltat) + (0.5 * (shipaccy) * m.pow(deltat,2))
    m1 = ship.velocity.x + shipaccx*deltat
    n1 = ship.velocity.y + shipaccy*deltat
    k2 = ship.pos.x + ((ship.velocity.x + 0.5*deltat*m1) * (0.5*deltat) + (0.5 * (shipaccx) * m.pow(0.5*deltat,2)))
    l2 = ship.pos.y + ((ship.velocity.y + 0.5*deltat*n1) * (0.5*deltat) + (0.5 * (shipaccy) * m.pow(0.5*deltat,2)))
    m2 = (ship.velocity.x + 0.5*deltat*m1) + 0.5*shipaccx*deltat
    n2 = (ship.velocity.y + 0.5*deltat*n1) + 0.5*shipaccy*deltat
    k3 = ship.pos.x + ((ship.velocity.x + 0.5*deltat*m2) * (0.5*deltat) + (0.5 * (shipaccx) * m.pow(0.5*deltat,2)))
    l3 = ship.pos.y + ((ship.velocity.y + 0.5*deltat*n2) * (0.5*deltat) + (0.5 * (shipaccy) * m.pow(0.5*deltat,2)))
    m3 = (ship.velocity.x + 0.5*deltat*m2) + 0.5*shipaccx*deltat
    n3 = (ship.velocity.y + 0.5*deltat*n2) + 0.5*shipaccy*deltat
    k4 = ship.pos.x + ((ship.velocity.x + deltat*m3) * (deltat) + (0.5 * (shipaccx) * m.pow(deltat,2)))
    l4 = ship.pos.y + ((ship.velocity.y + deltat*n3) * (deltat) + (0.5 * (shipaccy) * m.pow(deltat,2)))
    m4 = (ship.velocity.x + deltat*m3) + shipaccx*deltat
    n4 = (ship.velocity.y + deltat*n3) + shipaccy*deltat
    
    
    ship.pos.x = ship.pos.x + ((deltat / 6) * (k1 + 2*k2 + 2*k3 + k4))
    ship.pos.y = ship.pos.y + ((deltat / 6) * (l1 + 2*l2 + 2*l3 + l4))
    ship.velocity.x = ship.velocity.x + ((deltat / 6) * (m1 + 2*m2 + 2*m3 + m4))
    ship.velocity.y = ship.velocity.y + ((deltat / 6) * (n1 + 2*n2 + 2*n3 + n4))
    
    ##print("x=",ship.pos)
    ##print("v=",ship.velocity)
    
    ##Leave an Orbit Line
    ship.trail.append(pos=ship.pos)
    
    ##Increment Time
    t = t + deltat