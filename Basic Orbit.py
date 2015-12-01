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
deltat = 0.00001

##Earth Constants
earth = sphere(pos=[0,0],radius=6000,color=(0,0.5,0.5))
earthmass = 5972000000000000000000000

##Ship Initial Conditions
ship = sphere(pos=[7000,0],radius=50,color=color.red)
ship.velocity = vector(0,300000)
shipmass = 75000
ship.trail = curve(color=ship.color)

while t < 1000:
    rate(1000)
    
    ##Get the ship's current Location
    shipdist = m.sqrt(m.pow(ship.pos.x,2)+m.pow(ship.pos.y,2))
    
    ##Calculate Acceleration
    shipacc = (G * earthmass) / m.pow(shipdist,2)
    shipaccx = shipacc * (-ship.pos.x / shipdist)
    shipaccy = shipacc * (-ship.pos.y / shipdist)
    
    ##Update Ship's Position
    ship.pos.x = ship.pos.x + (ship.velocity.x * deltat) + (0.5 * (shipaccx) * m.pow(deltat,2))
    ship.pos.y = ship.pos.y + (ship.velocity.y * deltat) + (0.5 * (shipaccy) * m.pow(deltat,2))
    
    ##Update Ship's Velocity
    ship.velocity.x = ship.velocity.x + shipaccx*deltat
    ship.velocity.y = ship.velocity.y + shipaccy*deltat
    
    ##Leave an Orbit Line
    ship.trail.append(pos=ship.pos)
    
    ##Increment Time
    t = t + deltat

    
