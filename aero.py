import numpy as np
from geometry import *
from interpolate_cl import *
from velocity import *


def aeroload(theta, w0 ,V, r):
    u_r = omega(theta, w0) * r
    w = np.sqrt(V**2 + u_r**2)
    print(w)

    beta = np.degrees(np.arctan2(V, u_r))
    alpha = twist_angle(r)
    delta = beta - alpha
    print(delta)

    cl = cl_cubic(delta)
    print(cl)
    cw = cw_cubic(delta)
    epsilon = np.degrees(np.arctan2(cw, cl))

    T = 0.5 * rho_air * w**2 * chord_width * np.sqrt(cl**2 + cw**2)*np.sin(np.deg2rad(beta - epsilon))*vib_fac_per
    A = 0.5 * rho_air * w**2 * chord_width * np.sqrt(cl**2 + cw**2)*np.cos(np.deg2rad(beta - epsilon))*vib_fac_par
    print(cw)

    return T, A
# print(aeroload(2.62, 13, 4.43))