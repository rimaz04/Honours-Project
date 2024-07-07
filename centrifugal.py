import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from geometry import *

def normal_force(omega, r):
    r_end = 10.975

    rho = 7800 # kg/m^3


    # integrating r*dm from r to r_end
    I = integrate.quad(lambda x: rho*x*cross_sectional_area(x), r, r_end)
    n = omega**2 * I[0]
    return n

print(normal_force(2.62, 0))


