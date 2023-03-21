import numpy as np
import plotly.graph_objs as go

# Define the range of theta and phi values
theta_range = np.linspace(0, 2 * np.pi, 100)
phi_range = np.linspace(0, np.pi, 100)

# Create a meshgrid of theta and phi values
theta, phi = np.meshgrid(theta_range, phi_range)

# Calculate the spherical harmonics Y_3^2 for each (theta, phi) pair
Y_3_2 = np.sqrt(15 / (32 * np.pi)) * np.sin(phi) ** 2 * np.exp(2j * 3 * theta)

# Convert the spherical coordinates (theta, phi, r) to Cartesian coordinates (x, y, z)
x = np.real(Y_3_2 * np.sin(phi) * np.cos(theta))
y = np.real(Y_3_2 * np.sin(phi) * np.sin(theta))
z = np.real(Y_3_2 * np.cos(phi))

# Create a 3D surface plot of the spherical harmonics using Plotly
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
fig.update_layout(title='Spherical Harmonics Y_3^2')
fig.show()
