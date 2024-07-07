import numpy as np
import matplotlib.pyplot as plt

def omega(theta,w0):
    # Parameters
    v0 = w0*10.975  # initial velocity
    r = 10.975    # radius of the circle
    g = 9.81   # acceleration due to gravity

    v = np.sqrt(v0**2 + 2 * g * r * np.cos(theta))
    return v/r

