import numpy as np
from wisdem.turbinesfst.turbine import Turbine

# Define the turbine parameters
rotor_radius = 40.0  # m
wind_speed = 8.0     # m/s
pitch_angle = 0.0    # deg
rpm = 12.0           # rpm

# Create the turbine object
turbine = Turbine(rotor_radius)

# Set the operating conditions
turbine.set_operating_conditions(wind_speed, pitch_angle, rpm)

# Compute the flow field
flow_field = turbine.compute_flow_field()

# Extract the results
pressure = flow_field.pressure
velocity = flow_field.velocity
forces = turbine.get_forces()

# Print the results
print("Pressure:", pressure)
print("Velocity:", velocity)
print("Forces:", forces)