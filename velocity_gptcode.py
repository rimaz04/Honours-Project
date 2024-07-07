import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

# Parameters
r = 10.975       # radius of the circle
g = 9.81      # acceleration due to gravity
dt = 0.01     # time step
T = 1.0       # total time
theta_total = 1.0 * np.pi  # known total theta in 1 second (one full rotation)

def final_theta_difference(v0, r, g, dt, T, theta_total):
    # Time array
    time = np.arange(0, T, dt)
    
    # Initialize theta and velocity
    theta = 0.0
    velocity = v0
    
    for t in time[1:]:
        # Compute theta
        theta += (velocity / r) * dt
        # Compute velocity
        velocity = np.sqrt(v0**2 + 2 * g * r * np.cos(theta))
        if t >= T:
            break
    
    # Return the difference between computed theta and total theta
    return theta - theta_total

# Use root-finding to find the initial velocity v0
solution = root_scalar(final_theta_difference, args=(r, g, dt, T, theta_total), bracket=[0.1, 100.0], method='bisect')

if solution.converged:
    v0 = solution.root
    print(f"Initial velocity v0 to achieve theta_total of {theta_total} radians after 1 second is: {v0:.4f} m/s")
else:
    print("Root-finding did not converge")

# Plotting the results using the found initial velocity
time = np.arange(0, T, dt)
theta = np.zeros_like(time)
velocity = np.zeros_like(time)
velocity[0] = v0

for i in range(1, len(time)):
    theta[i] = theta[i-1] + (velocity[i-1] / r) * dt
    velocity[i] = np.sqrt(v0**2 + 2 * g * r * np.cos(theta[i]))

# Plotting the results
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(time, theta)
plt.title('Angle (theta) vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Theta (radians)')

plt.subplot(2, 1, 2)
plt.plot(time, velocity)
plt.title('Velocity (v) vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')

plt.tight_layout()
plt.show()
