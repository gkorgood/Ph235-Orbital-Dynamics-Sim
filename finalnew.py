# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:14:28 2015

@author: Gabe
"""

from __future__ import division,print_function
import math as m
from visual import *

##Constants
G = 0.0000000000667408
t = 0
deltat = 0.3

##Earth Constants
earth = sphere(pos=[0,0],radius=6371000,color=(0,0.5,0.5))
earthmass = 5972000000000000000000000

##Ship Initial Conditions
ship = sphere(pos=[-20000000,0],radius=5000,color=color.red)
ship.velocity = vector(0,-3200)##m.sqrt(G * earthmass / ship.pos.x)
shipdist = m.sqrt(m.pow(ship.pos.x,2)+m.pow(ship.pos.y,2))
veltot = m.sqrt(m.pow(ship.velocity.x,2)+m.pow(ship.velocity.y,2))
##print("v=",ship.velocity)
shipmass = 75000
ship.trail = curve(color=ship.color)

##Energy Check
U = (-G * earthmass * shipmass)/shipdist
K = 0.5 * shipmass * (m.pow(veltot,2))
print(U+K)
##E = text(text='The energy of the ship is: %f' % (U+K),align='right', pos=(10000,0), height = 2000, depth=0.01, color=color.white)

while t < 100000:
    rate(1000)
    
    ##Get the ship's current Location, Velocity, and Energy
    shipdist = m.sqrt(m.pow(ship.pos.x,2)+m.pow(ship.pos.y,2))
    veltot = m.sqrt(m.pow(ship.velocity.x,2)+m.pow(ship.velocity.y,2))
    U = (-G * earthmass * shipmass)/shipdist
    K = 0.5 * shipmass * (m.pow(veltot,2))
    ##E.text = 'The energy of the ship is: %f' % (U+K)
    print(U+K)
    
    ##Calculate Acceleration
    shipacc = (G * earthmass) / m.pow(shipdist,2)
    shipaccx = shipacc * (-ship.pos.x / shipdist)
    shipaccy = shipacc * (-ship.pos.y / shipdist)
    
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