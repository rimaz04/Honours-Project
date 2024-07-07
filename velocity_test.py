import numpy as np
import matplotlib.pyplot as plt

# # Parameters
# v0 = 20  # initial velocity
# r = 10.975    # radius of the circle
# g = 9.81   # acceleration due to gravity
# dt = 0.01  # time step
# T = 10.0   # total time

# # Time array
# time = np.arange(0, T, dt)

# # Arrays to store theta and velocity
# theta = np.zeros_like(time)
# velocity = np.zeros_like(time)
# velocity[0] = v0

# # Numerical integration using Euler method
# for i in range(1, len(time)):
#     # Compute theta
#     theta[i] = theta[i-1] + (velocity[i-1] / r) * dt
#     # Compute velocity
#     velocity[i] = np.sqrt(v0**2 + 2 * g * r * np.cos(theta[i]))

# # Find average velocity in time T
# average_velocity = np.mean(velocity)
# print('Average velocity:', average_velocity)

# # Plotting the results
# plt.figure(figsize=(10, 5))
# plt.subplot(2, 1, 1)
# plt.plot(time, theta)
# plt.title('Angle (theta) vs Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Theta (radians)')

# plt.subplot(2, 1, 2)
# plt.plot(time, velocity)
# plt.title('Velocity (v) vs Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Velocity (m/s)')

# plt.show()
