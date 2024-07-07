import numpy as np
from geometry import *
from mat_prop import *
from scipy import integrate

def mass(r): # finds weight of the blade between r and r_end
    r_end = 10.975
    # integrating dm from r to r_end
    I = integrate.quad(lambda x: rho*cross_sectional_area(x), r, r_end)
    m = I[0]
    return m

def weight_tan(theta, r):
    return mass(r)*g*np.sin(theta)
