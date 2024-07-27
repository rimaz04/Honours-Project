# import numpy as np
# from scipy import interpolate
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Placeholder for material properties (density)
# class mat_prop:
#     rho = 7850  # Example density for steel in kg/m^3

# # Define the width function
# def width(r):
#     if np.isscalar(r):
#         if r < 1.100:
#             return 0.310
#         z = [1.100, 10.975]
#         x = [0.310, 0.200]
#         w = interpolate.interp1d(z, x, fill_value="extrapolate")
#         return w(r)
#     else:
#         r = np.asarray(r)
#         w = np.where(r < 1.100, 0.310, interpolate.interp1d([1.100, 10.975], [0.310, 0.200], fill_value="extrapolate")(r))
#         return w

# # Define the twist angle function
# def twist_angle(r):
#     angle = [18, 18.4, 18.8, 19, 19.1, 19.1, 19, 18.8, 18.5, 18.1, 17.6, 17, 16.2, 15.4, 14.4, 13.3, 12.1, 10.8, 9.3, 7.7, 6, 4.1, 1.9, -0.5, -3.1, -6]
#     r_start = 1.2
#     r_end = 10.975
#     phi = interpolate.interp1d(np.linspace(r_start, r_end, len(angle)), np.deg2rad(angle), fill_value="extrapolate")
#     if np.isscalar(r):
#         return 0 if r < r_start else phi(r)
#     else:
#         r = np.asarray(r)
#         return np.where(r < r_start, 0, phi(r))

# # Define the height function
# def height(r):
#     if np.isscalar(r):
#         if r < 1.2:
#             return 0.35, 0, 0.35, 0
#     else:
#         r = np.asarray(r)
#         if np.all(r < 1.2):
#             return np.array([0.35]*len(r)), np.zeros(len(r)), np.array([0.35]*len(r)), np.zeros(len(r))
    
#     z = [1.2, 10.975]
#     h_back_top_values = [0.350, 0.700]
#     h_back_bottom_values = [0, 0.6]
#     h_back_top_interp = interpolate.interp1d(z, h_back_top_values, fill_value="extrapolate")
#     h_back_bottom_interp = interpolate.interp1d(z, h_back_bottom_values, fill_value="extrapolate")
#     h_back_top = h_back_top_interp(r)
#     h_back_bottom = h_back_bottom_interp(r)
#     h_front_top = h_back_top - np.tan(twist_angle(r)) * width(r)
#     h_front_bottom = h_back_bottom - np.tan(twist_angle(r)) * width(r)
#     return h_back_top, h_back_bottom, h_front_top, h_front_bottom

# # Create the 3D surface model
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# r = np.linspace(0, 10.975, 100)
# w = np.linspace(0, 0.310, 100)
# r_grid, w_grid = np.meshgrid(r, w)

# h_back_top_grid = np.zeros_like(r_grid)
# h_back_bottom_grid = np.zeros_like(r_grid)
# h_front_top_grid = np.zeros_like(r_grid)
# h_front_bottom_grid = np.zeros_like(r_grid)

# for i in range(r_grid.shape[0]):
#     for j in range(r_grid.shape[1]):
#         h_back_top, h_back_bottom, h_front_top, h_front_bottom = height(r_grid[i, j])
#         h_back_top_grid[i, j] = h_back_top
#         h_back_bottom_grid[i, j] = h_back_bottom
#         h_front_top_grid[i, j] = h_front_top
#         h_front_bottom_grid[i, j] = h_front_bottom

# # Calculate the z coordinates for the back and front surfaces
# z_back1 = h_back_top_grid 
# z_back2 = h_back_bottom_grid
# z_front1 = h_front_top_grid
# z_front2 = h_front_bottom_grid

# # Plot the back and front surfaces
# ax.plot_surface(r_grid, w_grid, z_back1, alpha=0.5, color='b')
# # ax.plot_surface(r_grid, w_grid, z_back2, alpha=0.5, color='r')
# ax.plot_surface(r_grid, w_grid, z_front1, alpha=0.5, color='g')
# #ax.plot_surface(r_grid, w_grid, z_front2, alpha=0.5, color='y')


# ax.set_xlabel('Blade Length (m)')
# ax.set_ylabel('Width (m)')
# ax.set_zlabel('Height (m)')
# ax.set_title('3-D Surface Visualization of the Windmill Beam')

# plt.show()

import numpy as np
from scipy import interpolate, integrate
import mat_prop as mp


def width(r):
    if r < 1.100:
        return 0.360
    
    z = [1.100, 12.6]
    x = [0.360, 0.190]

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
        h_back_top = 0.46
        h_back_bottom = 0
        h_front_top = 0.46
        h_front_bottom = 0
        # h_back = h_back_top - h_back_bottom
        # h_front = h_front_top - h_front_bottom
        return h_back_top, h_back_bottom, h_front_top, h_front_bottom
    z = [1.2, 12.6]
    h_back_top = [0.460, 0.920]
    h_back_bottom = [0, 0.830]
    h_back_top = interpolate.interp1d(z, h_back_top)
    h_back_bottom = interpolate.interp1d(z, h_back_bottom)
    # h_back = h_back_top(r) - h_back_bottom(r)
    h_front_top = h_back_top(r) #- np.tan(twist_angle(r)) * width(r)
    h_front_bottom = h_back_bottom(r) #- np.tan(twist_angle(r)) * width(r)
    # h_front = h_front_top - h_front_bottom
    return h_back_top(r), h_back_bottom(r), h_front_top, h_front_bottom

def thickness(r):
    z_top = np.cumsum([0, 1.1, 2.635, 2.160, 8.080])
    t_top = [0.01, 0.008, 0.006, 0.004]
    pos_top = np.searchsorted(z_top, r)
    z_front = np.cumsum([0, 1.2, 2.635, 2.160, 8.080])
    t_front = [0.01, 0.008, 0.006, 0.004]
    pos_front = np.searchsorted(z_front, r)
    if r == 0:
        return t_top[0], t_front[0]
    return t_top[pos_top - 1], t_front[pos_front - 1]

def cross_sectional_area(r):
    h_back_top, h_back_bottom, h_front_top, h_front_bottom = height(r)
    t_top, t_front = thickness(r)
    w = width(r)

    A = 1/2 * ((h_back_top - h_back_bottom) + (h_front_top - h_front_bottom)) * w - 1/2 * (((h_back_top - h_back_bottom - 2*t_top)) + ((h_front_top - h_front_bottom - 2*t_top))) * (w - 2*t_front)
    return A

def mass(r):
    r_end = 12.6

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