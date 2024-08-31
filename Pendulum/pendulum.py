import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Physical Constants
g = 9.81 # acceleration due to gravity (m/s^2)
L = 1.0 # length of pendulum (m)
mu = 0.1 # resistance coefficient

# Initial Conditions
theta_0 = np.pi / 4 # initial angle in radians
theta_dot_0 = 0 # initial angular velocity

# Simulation time
simulation_time = 10

# Definition of ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta)

# Solution to the differential equation
def theta(t):
    #Initialize changing values
    theta = theta_0
    theta_dot = theta_dot_0
    dt = 0.01 # time step
    theta_values = [theta]

    for t in np.arange(0, t, dt):
        theta_double_dot = get_theta_double_dot(
            theta, theta_dot
        )
        # Euler's method
        theta += theta_dot * dt
        theta_dot += theta_double_dot * dt
        theta_values.append(theta)

    return np.array(theta_values)

# Animation Parameters
fig, ax = plt.subplots()
ax.set_xlim(-2 * L, 2 * L)
ax.set_ylim(-2 * L, 2 * L)

line, = ax.plot([], [], 'o-', lw=2, color='black', markersize=10)
ax.set_facecolor('white')
ax.grid(True)
ax.axis('off')

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function: called sequentially to update the plot
def animate(i):
    # Use the global simulation_time variable
    theta_values = theta(simulation_time)  # Compute values
    x = L * np.sin(theta_values[i])
    y = -L * np.cos(theta_values[i])
    line.set_data([0, x], [0, y])
    return line,

# Call the animator using the simulation_time variable
ani = FuncAnimation(fig, animate, frames=len(theta(simulation_time)), 
                    init_func=init, blit=True)

# Save the animation as an MP4
ani.save('pendulum_simulation.mp4', writer='ffmpeg', fps=60)

plt.show()
