import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

n_nodes = 9
max_wind = 13
rho_air = 1.225 # kg m^-3 # air density
g = 9.80665 # m s^-2 # gravitational acceleration
vib_fac_par = 1.1
vib_fac_per = 1.0

# Define wind speed
v_wind = np.ones(n_nodes) * max_wind

# Define the tangential component
u_r = np.array([19.55, 16.90, 22.19, 24.84, 14.25, 27.48, 11.61, 8.96, 6.31])

# Define angles
a = np.array([15.0, 18.0, 10.8, 5.4, 19.4, -0.60, 20.20, 20.80, 19.60])
b = np.degrees(np.arctan2(v_wind, u_r))
d = b - a
# print(delta)

# Define aerodynamic coefficients
cl_list = np.array([1.11, 1.24, 1.30, 1.31, 1.29, 1.29, 1.30, 1.31, 1.31])
cw_list = np.array([0.75, 0.58, 0.48, 0.40, 0.32, 0.32, 0.34, 0.35, 0.42])

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].plot(d, cl_list, 'r')
ax[0].set_title('Lift Coefficient vs AoA')
ax[0].set_xlabel('Delta, [deg]')
ax[0].set_ylabel('Lift Coefficient, [-]')
ax[0].grid()

ax[1].plot(d, cw_list, 'b')
ax[1].set_title('Drag Coefficient vs AoA')
ax[1].set_xlabel('Delta, [deg]')
ax[1].set_ylabel('Drag Coefficient, [-]')
ax[1].grid()

# plt.tight_layout()
# plt.show()

# Interpolate the aerodynamic coefficients

cl_cubic = sp.interpolate.interp1d(x=d, y=cl_list, kind='cubic')
cw_cubic = sp.interpolate.interp1d(x=d, y=cw_list, kind='cubic')

# cw_test = cw_cubic(28)
# print(cw_test)