Name: Peter Sullivan (psulli29)

Module Info: 

Module 4, Assignment 1. nbody.py
DueDate - 9/24/23

Approach:

nbody.py

For this problem we first initialize the input and starting information as variables. We have t, which is our total time of the simulation. dt, which is our delta step as we process through the simulation. We have five lists, earth, mars, mercury, sun and venus. These lists consist of 5 elements, x and y position, x and y velocity, and finally the mass respectively. I then created a variable called time_total, which is the initial start time for the while loop. The variable G is the gravitational constant that will be used in the force calculation.

Next, I create a nested list of the planets using the 5 lists of planets called planets. This will allow me to loop through each planet and grab their respective info in the while loop below.

I then initialize the while loop. We keep looping through until our time_total variable is >= to t variable. Next I create a for loop using the range and len function with the planets list. This will loop through the indexs at the length of the list provided. Since there are 5 items in the loop, we will go through the 4 loop 5 times.

Next, I put in a if loop to check if the list item in planets is the sun, if the item is the sun then I use the statement continue. Continue allows for the for-loop to jump to the next item and skip all the statements all below for the sun list.

Now we start going through the process of calculating the new x and y position and velocities for each planet based on the new timestep. We first create the dx and dy variables using the suns location and the planets current location. Note that the sun is subtracting the planets location. This is done to get the correct sign of delta x and y, which will affect the calculations down the line. Next, we create the radius variable using the dx and dy variables we just created. Next I create the total_force variable using the G variable, the current planets mass and the suns mass, and radius variable.

Once we have the total force, we can calculate the x and y components of the force using the total force, the delta x and y, and the radius, and name them as the variables fx and fy. The fx and fy variables now allow us to calculate the x and y components of acceleration. I named those ax and ay. These are calculated using the fy or fy variables with the current planet’s mass.

Now that we have the acceleration components, we can now calculate the new velocity in the x and y direction. For this, we use the old velocity of the planet which is currently in the planet list, and the components of the acceleration and the current timestep. For this I named them vx_new and vy_new.


With the new x and y components of the velocity, vx_new and vy_new, we can now calculate the new x and y positions for that planet. We calculate this using the old positions (which is found in the planets list),  the vx_new or vy_new variables and the delta time step. I name these variables dx_new and dy_new.

Now we need to update the planets list for that current planet in the for loop. I update each component of the list, excluding the mass (mass does not change in this simulation). I update each item in the list with the new x and y positions/velocities. (dx_new, dy_new, vx_new and vy_new).

Now that we have updated each planet with new positions and velocities for every planet in the list. We now exit the for loop. I then update the time_total variable by taking the current total_time variable and adding the dt variable to it (the time step). We then go back to the top of the while loop and check to see if total time is >= t, if not, the loop goes through the process listed above until time_total is greater then the t variable.

Once the while loop ends, I then created a for loop using the range, and len functions with the planets list. In each loop, I utilize the print function and a f string to print out the items in the list. I grab each item from their index 0 to 4. To get the scientific notation and the number of decimals in the fstring, I utilized the resource provided in the homework: https://zetcode.com/python/fstring/. We first use a colon after the variable or value in the fstring. I then specify the number of decimal places using the “.” and a number after the period. So for this homework, we wanted 4 decimals, so it’s :.4. I then wanted the scientific notation. To get this, I used the e after the :.4. So it comes out to {variable:.4e}. I did this for every index in a print statement for every planet in the planets list.


Known Bugs:
N/A
