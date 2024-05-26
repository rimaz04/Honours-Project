


# Geomteric properties of the beams

l_b_z = 5 # length of the beam in m
l_b_y = 0.2 # width of the beam in m
l_b_x = 0.2 # height of the beam in m
t = 0.02 # thickness of the beam in m

# Geometric properties of the grid

l_g_z = 5 # length of the grid in m
l_g_y = 1 # width of the grid in m
l_g_x = 0.2 # height of the grid in m


grid_z0 = 0.5 # distance to the first grid node in m
n_grid = 31 # number of attachement grid points

I_xx = ((l_b_y)**3 * l_b_x)/12 - ((l_b_y - 2*t)**3 * (l_b_x - 2*t))/12 # moment of inertia in m^4
I_yy = ((l_b_x)**3 * l_b_y)/12 - ((l_b_x - 2*t)**3 * (l_b_y - 2*t))/12 # moment of inertia in m^4
I_zz = 0

J_z = l_b_y**3 * l_b_x * (1/3 - 0.21 * (l_b_y/l_b_x) * (1 - (l_b_y**4)/(12*l_b_x**4))) # torsional constant in m^4


