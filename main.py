# Compute Tidal Force Upon Body
# G Gravitatonal constant, km³/s² per solar mass
# M is the Black Hole Mass, solar masses
# L id the distanca between two points , km
# C is the circumference , km
# A is difference in acceleration, km/sec²
import math
import numpy as np

C = 10000
G = 1.327E11
pi = 3.14159
M = 303

for L in np.arange(0.0018, 0.004, 0.001):
    A = 16*pi*pi*pi*G*M*L / (C*C*C)

    A = (A*1000)/9.81
    print("Length: ", L, "km, Tidal Force: ", A, "g")
