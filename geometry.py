import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate


# create function that gives alpha for a certain r

def alpha(r):
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

def width(r):
    if r < 1.100:
        return 0.310
    
    z = [1.100, 10.975]
    x = [0.310, 0.200]

    w = interpolate.interp1d(z, x)
    return w(r)


def twist_angle(r):
    angle = [18, 18.4, 18.8, 19, 19.1, 19.1, 19, 18.8, 18.5, 18.1, 17.6, 17, 16.2, 15.4, 14.4, 13.3, 12.1, 10.8, 9.3, 7.7, 6, 4.1, 1.9, -0.5, -3.1, -6]
    r_start = 0
    r_end = 10.975
   
    # interpolate the angle
    phi = interpolate.interp1d(np.linspace(r_start, r_end, len(angle)), np.deg2rad(angle))
    if r < r_start:
        return 0
    else:
        # return angle at r
        return phi(r)

chord_width = 2.5 # m

def height(r):
    if r < 0.35:
        h_back_top = 0.35
        h_back_bottom = 0
        h_front_top = 0.35
        h_front_bottom = 0
        # h_back = h_back_top - h_back_bottom
        # h_front = h_front_top - h_front_bottom
        return h_back_top, h_back_bottom, h_front_top, h_front_bottom
    z = [0.35, 10.975]
    h_back_top = [0.350, 0.700]
    h_back_bottom = [0, 0.6]
    h_back_top = interpolate.interp1d(z, h_back_top)
    h_back_bottom = interpolate.interp1d(z, h_back_bottom)
    # h_back = h_back_top(r) - h_back_bottom(r)
    h_front_top = h_back_top(r) - twist_angle(r) * width(r)
    h_front_bottom = h_back_bottom(r) - twist_angle(r) * width(r)
    # h_front = h_front_top - h_front_bottom
    return h_back_top(r), h_back_bottom(r), h_front_top, h_front_bottom

def thickness(r):
    z_top = [1.1, 2.635, 2.160, 5.080]
    t_top = [0.01, 0.008, 0.006, 0.004]
    pos_top = np.searchsorted(z_top, r)
    z_front = [1.1, 2.635, 2.160, 5.080]
    t_front = [0.01, 0.008, 0.006, 0.004]
    pos_front = np.searchsorted(z_front, r)

    return t_top[pos_top - 1], t_front[pos_front - 1]

def cross_sectional_area(r):
    h_back_top, h_back_bottom, h_front_top, h_front_bottom = height(r)
    t_top, t_front = thickness(r)
    w = width(r)
    
    A = 1/2 * ((h_back_top - h_back_bottom) + (h_front_top - h_front_bottom)) * w * alpha(r) - 1/2 * (((h_back_top - t_top) - (h_back_bottom - t_top)) - ((h_front_top - t_top) - (h_front_bottom - t_top))) * (w - 2*t_front) *alpha(r)

    return A

print(cross_sectional_area(0))
