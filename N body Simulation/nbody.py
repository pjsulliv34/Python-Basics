"""
This program simulates the movement of the planets, earth, mars, mercury, and Venus around
the sun using x and y components. At steps of 25000, we simulate the movement of these planets
in roughly 7000 steps. For each step we calculate the Total force between the planet and the sun. We
then calculate the x and y components of the force. Next, we calculate the x and y components of the
acceleration of that planet. Using the acceleration, we then calculate the x and y components of velocity.
Finally we can calculate the new x and y position, using the new velocity components that were just
calculated. We then update the velocity and x components with the information that we just calculated
that is used for the next step in the simulation.

"""

#Initial Input information
t = 157788000 # total time of simulation
dt = 25000 # time delta
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

time_total = 0 #initial starting time
G = 6.67E-11   # Gravitational constant

# Creating a list of the input information
planets = [earth,mars,mercury,sun,venus]


#Initial While loop, that allows us to loop through the simulaiton at timesteps
while time_total < t:
    #For loop to loop through the planets list
    for i in range(len(planets)):
        # this line below allows us to skip the sun
        if planets[i][4]==1.9890e+30:
            continue

        # Calculate the delta x and corresponding radius
        dx = planets[3][0] - planets[i][0]
        dy = planets[3][1] - planets[i][1]
        radius = (dx**2+dy**2)**(1/2)

        # Calculate the total force between planet and sun, using radius
        total_force = (G*planets[i][4]*planets[3][4])/(radius**2)

        # Calculate x and y components of Force, using total force
        fx = total_force*(dx/radius)
        fy = total_force*(dy/radius)

        # Calculate x and y components of Acceleration, using force components and mass
        ax  = fx/planets[i][4]
        ay = fy/planets[i][4]

        #Calculate the new velocity of planet using original velocity and acceleration
        vx_new = planets[i][2] + ax*dt
        vy_new = planets[i][3] + ay*dt

        # Calculate new position based on old position and new velocity
        dx_new = planets[i][0]+vx_new*dt
        dy_new = planets[i][1]+vy_new*dt

        #Replace x and y components of planets for position and velocity, inplace for list
        planets[i][0] = dx_new
        planets[i][1] = dy_new
        planets[i][2] = vx_new
        planets[i][3] = vy_new

    # update the time by delta_t, this is neccessary so that the loop will end
    time_total += dt

#Loop through the planet list and print out using scientific notiation with 4 decimals
for i in range(len(planets)):
    print(f'{planets[i][0]:.4e} {planets[i][1]:.4e} {planets[i][2]:.4e} {planets[i][3]:.4e} {planets[i][4]:.4e}')