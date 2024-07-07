import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from geometry import *

def normal_force(omega, r):
    r_end = 10.975

    rho = 7800 # kg/m^3
    dm = rho* cross_sectional_area(x)

    # integrating r*dm from r to r_end
    I = integrate.quad(lambda r: x*dm, r, r_end)
    return I[0]
    n = omega**2 * I[0]
    return n

