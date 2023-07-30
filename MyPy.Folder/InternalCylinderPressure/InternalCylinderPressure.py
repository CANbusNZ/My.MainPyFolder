import matplotlib.pyplot as plt

# Given data
piston_diameter = 140 # mm
rod_diameter = 80 # mm
initial_volume = 4.15 # L
initial_pressure = 1 # bar
final_volume = 3.8 # L
bulk_modulus = 1500 # MPa

# Calculate the area of the piston and rod
piston_area = (3.1415 * (piston_diameter ** 2)) / 4
rod_area = (3.1415 * (rod_diameter ** 2)) / 4

# Calculate the effective area
effective_area = piston_area - rod_area

# Convert initial pressure from bar to MPa
initial_pressure_mpa = initial_pressure * 0.1

# Calculate the change in volume
delta_volume = initial_volume - final_volume

# Calculate the change in pressure using the bulk modulus formula
delta_pressure = (bulk_modulus * delta_volume) / initial_volume

# Calculate the final pressure in MPa
final_pressure_mpa = initial_pressure_mpa + delta_pressure

# Convert final pressure from MPa to bar
final_pressure_bar = final_pressure_mpa * 10

# Plot the results
plt.plot([initial_volume, final_volume], [initial_pressure, final_pressure_bar])
plt.xlabel('Volume (L)')
plt.ylabel('Pressure (bar)')
plt.title('Hydraulic Cylinder Compression')
plt.show()
