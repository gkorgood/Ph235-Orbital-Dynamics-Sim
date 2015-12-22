## Orbital Dynamics Simulation
12/21/15 | Gabriel Korgood | Cooper Union
-------- | --------------- | ------------


##### GENERAL INFORMATION
_________________________

These pieces of code simulate the movement of a spacecraft within two different gravitational systems, one with a single parent planet, and one with two planets of equal mass.

##### INSTALLATION & OPERATION
______________________________

Requires some way to open and run Python (.py) files, including the VPython and Math libraries. Download the .zip from the [project page](https://github.com/gkorgood/Ph235-Orbital-Dynamics-Sim). Open any of the three .py files (NOTE: 3bodyRK4.py attempts to run the simulation using a fourth order Runge-Kutta method, but is currently non-functional) in a Python IDE, and run them normally.

##### FILE MANIFEST
___________________

- ~\Ph235-Orbital-Dynamics-Sim\
  - \2bodyRK1.py\
  - \3bodyRK1.py\
  - \3bodyRK4.py\
  - \README.md\

##### INITIAL GOALS & CURRENT PROGRESS
______________________________________

- [ ] ~~Ascent from Earth's surface~~        (Abandoned due to complexity of atmospheric drag)
- [ ] Circularization burn               (Postponed due to complexity of rocket equation)
- [x] Demonstration of stable Earth orbit
- [ ] Transfer burn to solar orbit           (Postponed due to complexity of rocket equation)
- [ ] Transfer burn to binary system         (Postponed due to complexity of rocket equation)
- [x] Demonstration of chaotic binary orbit
