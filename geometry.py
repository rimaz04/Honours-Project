import numpy as np
from scipy import interpolate, integrate
import mat_prop as mp


def width(r):
    if r < 1.100:
        return 0.310
    
    z = [1.100, 10.975]
    x = [0.310, 0.200]

    w = interpolate.interp1d(z, x)
    return w(r)


def twist_angle(r):
    angle = [18, 18.4, 18.8, 19, 19.1, 19.1, 19, 18.8, 18.5, 18.1, 17.6, 17, 16.2, 15.4, 14.4, 13.3, 12.1, 10.8, 9.3, 7.7, 6, 4.1, 1.9, -0.5, -3.1, -6]
    r_start =0
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
    if r < 1.2:
        h_back_top = 0.35
        h_back_bottom = 0
        h_front_top = 0.35
        h_front_bottom = 0
        h_back = h_back_top - h_back_bottom
        h_front = h_front_top - h_front_bottom
        return h_back, h_front
    z = [0.35, 10.975]
    h_back_top = [0.350, 0.700]
    h_back_bottom = [0, 0.6]
    h_back_top = interpolate.interp1d(z, h_back_top)
    h_back_bottom = interpolate.interp1d(z, h_back_bottom)
    h_back = h_back_top(r) - h_back_bottom(r)
    # h_front_top = h_back_top(r) - np.tan(twist_angle(r)) * width(r)
    # h_front_bottom = h_back_bottom(r) - np.tan(twist_angle(r)) * width(r)
    h_front = h_back
    return h_back, h_front

def thickness(r):
    z_top = np.cumsum([0, 1.1, 2.635, 2.160, 5.080])
    t_top = [0.01, 0.008, 0.006, 0.004]
    pos_top = np.searchsorted(z_top, r)
    z_front = np.cumsum([0, 1.2, 2.635, 2.160, 5.080])
    t_front = [0.01, 0.008, 0.006, 0.004]
    pos_front = np.searchsorted(z_front, r)
    if r == 0:
        return t_top[0], t_front[0]
    return t_top[pos_top - 1], t_front[pos_front - 1]

def cross_sectional_area(r):
    h_back, h_front = height(r)
    t_top, t_front = thickness(r)
    w = width(r)

    A = 1/2 * (h_back + h_front) * w - 1/2 * ((h_back - 2*t_top) + (h_front - 2*t_top)) * (w - 2*t_front)
    return A

def mass(r):
    r_end = 10.975

    # integrating r*dm from r to r_end
    m = integrate.quad(lambda x: mp.rho*cross_sectional_area(x), r, r_end)
    return m[0]

# def circum_ar(r):
#     hb = height(r)[0]-height(r)[1]
#     hf = height(r)[2]-height(r)[3]
#     w = width(r)
#     c = hb + hf + w + w
#     a = c*thickness(r)[0] - 4*thickness(r)[1]**2	
#     return a

# def mass2(r):
#     r_end = 10.975

#     # integrating dm from r to r_end
#     m = integrate.quad(lambda x: mp.rho*circum_ar(x), r, r_end)
#     return m[0]

print(f'\n \n The mass of half of the outer beam is {mass(0)} kg. \n \n')
# print(f'\n \n The mass of half of the outer beam is {mass2(0)} kg. \n \n')
# print(height(10.975)[0]-height(10.975)[1])
# print(thickness(10.975)[0])
# print((height(1.2)[0])-height(1.2)[1])
# print((height(1.2)[2])-height(1.2)[3])

# #plot h front and h back
# import matplotlib.pyplot as plt
# r = np.linspace(0, 10.975, 100)
# h_back_top = []
# h_back_bottom = []
# h_front_top = []
# h_front_bottom = []
# for i in r:
#     h_back_top.append(height(i)[0])
#     h_back_bottom.append(height(i)[1])
#     h_front_top.append(height(i)[2])
#     h_front_bottom.append(height(i)[3])

# plt.plot(r, h_back_top, label='h_back_top')
# #plt.plot(r, h_back_bottom, label='h_back_bottom')
# plt.plot(r, h_front_top, label='h_front_top')
# #plt.plot(r, h_front_bottom, label='h_front_bottom')
# plt.legend()
# plt.show()




