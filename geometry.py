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
    z1 = [0,10.975]
    y1 = [155, 100]

    z2 = [0,10.975]
    y2 = [-155, -100]

    f1 = interpolate.interp1d(z1, y1)
    f2 = interpolate.interp1d(z2, y2)
    w = f1(r) - f2(r)
    return w

def alpha_calc(r):
    angle = [18, 18.4, 18.8, 19, 19.1, 19.1, 19, 18.8, 18.5, 18.1, 17.6, 17, 16.2, 15.4, 14.4, 13.3, 12.1, 10.8, 9.3, 7.7, 6, 4.1, 1.9, -0.5, -3.1, -6]
    r_start = 1.975
    r_end = 10.975
    # interpolate the angle
    angle_interp = np.interp(r, np.linspace(r_start, r_end, len(angle)), angle)
    if r < r_start:
        return 0
    else:
        # return angle at r
        return angle_interp

chord_width = 2.5 # m
