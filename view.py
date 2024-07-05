import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def h_back_view(r):


    y1 = [0, 0, 0.6]
    z1 = [0, 1.2, 10.975]
    
    y2 = [0.35, 0.35, 0.7]
    z2 = [0, 1.2, 10.975]

    f1 = sp.interpolate.interp1d(x=z1, y=y1, kind='linear')
    f2 = sp.interpolate.interp1d(x=z2, y=y2, kind='linear')

    z_test = np.arange(0, 10.975, 0.1)

    h = f2(r) - f1(r)

    plt.plot(z_test, f1(z_test), 'r')
    plt.plot(z_test, f2(z_test), 'b')
    plt.title('Height of the back view')
    plt.xlabel('z, [m]')
    plt.ylabel('y, [m]')
    plt.show()
    return h

print(h_back_view(9.32))