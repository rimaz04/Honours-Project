import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate


# create function that gives alpha for a certain r

def alpha(r):
    angle = [18, 18.4, 18.8, 19, 19.1, 19.1, 19, 18.8, 18.5, 18.1, 17.6, 17, 16.2, 15.4, 14.4, 13.3, 12.1, 10.8, 9.3, 7.7, 6, 4.1, 1.9, -0.5, -3.1, -6]
    r_start = 1975
    r_end = 10975
    # interpolate the angle
    angle_interp = np.interp(r, np.linspace(r_start, r_end, len(angle)), angle)
    if r < r_start:
        return 0
    else:
        # return angle at r
        return angle_interp

def width(r):
    z = [0, 10.975]
    x = [310, 200]

    w = interpolate.interp1d(z, x)
    return w(r)


def twist_angle(r):
    angle = [18, 18.4, 18.8, 19, 19.1, 19.1, 19, 18.8, 18.5, 18.1, 17.6, 17, 16.2, 15.4, 14.4, 13.3, 12.1, 10.8, 9.3, 7.7, 6, 4.1, 1.9, -0.5, -3.1, -6]
    r_start = 0
    r_end = 10.975
   
    # interpolate the angle
    phi = np.interp(r, np.linspace(r_start, r_end, len(angle)), np.deg2rad(angle))
    if r < r_start:
        return 0
    else:
        # return angle at r
        return phi

chord_width = 2.5 # m

def height(r):
    h_front_top = [0]