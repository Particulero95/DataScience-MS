import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from scipy.special import genlaguerre, sph_harm

# Define the radial and angular wave functions
def hydrogen_1s(r):
    """
    Returns the value of the radial wave function for the hydrogen atom at the
    first excited state, given the radial coordinate r.
    """
    # Constants
    a0 = 1.0  # Bohr radius
    Z = 1.0   # Atomic number of hydrogen
    
    # Radial part of the wave function
    R = np.sqrt(2.0 / (a0**3 * np.sqrt(3))) * (2.0 - r / a0) * np.exp(-r / (2.0 * a0))
    
    return R

def hydrogen_1s_angular(theta, phi):
    """
    Returns the value of the angular wave function for the hydrogen atom at the
    first excited state, given the spherical angles (theta, phi).
    """
    # Angular part of the wave function
    Y = sph_harm(1, 0, theta, phi)
    
    return Y

# Define the grid of points at which to evaluate the wave function
r = np.linspace(0, 10, 100)
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
R, Theta, Phi = np.meshgrid(r, theta, phi, indexing='ij')
X = R * np.sin(Theta) * np.cos(Phi)
Y = R * np.sin(Theta) * np.sin(Phi)
Z = R * np.cos(Theta)

# Evaluate the wave function at each point on the grid
psi = hydrogen_1s(R) * hydrogen_1s_angular(Theta, Phi)

# Create a 3D surface plot of the wave function using Plotly
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])
fig.add_trace(go.Surface(x=X, y=Y, z=Z, surfacecolor=psi.real, colorscale='Viridis'),
              row=1, col=1)
fig.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
                  title='Hydrogen atom at the first excited state')
fig.show()

hydrogen_1s(2)
hydrogen_1s_angular(2*np.pi/3, np.pi/3)
