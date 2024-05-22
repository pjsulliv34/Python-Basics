"""
This program creates Point objects. Point objects can be used to plot figures and save the figures to current directory.
A point object takes in 4 arguments, a list of x/y coordinates [[x,y],[x1,y1]], a list of max points [[(x1,y1),(x2,y2)]].
and whether we want to show the plots. maxpoints is set by default to None and show is set to True as default. This
program has one method called plot. When creating the object in specifying the max points and whether show is true or
false will determine the plot method. The plot method sorts through the pairs of x/y coordinates and uses the
matplotlib.pyplot class to plot the x and y coordinates. The program then checks to see if max points is not set to None,
if so, the program then will plot lines for each set of max points. Then if the show is set to true, the program will
display the plot. Then the program will save the figure with the filename provided for the plot method, and finally
will clear the plot.
"""
# Import pyplot from matplotlib
from matplotlib import pyplot as plt

# Create Class Point
class Point:

    # Create an Point object with initial x/y coordinates, max_points, and collinear instances
    def __init__(self, x_y_coord, max_points = None, show = True):
        self.x_y_coord = x_y_coord
        self.max_points = max_points
        self.show = show

    # Create the Plot Method
    def plot(self, filename: str):

        # Initialize empty lists
        x = []
        y = []

        # For loop to loop through data points
        for i in self.x_y_coord:

            # Append x and y coordinates to respective lists
            x.append(i[0])
            y.append(i[1])

        # Plot the x and y coordinates in red circles
        plt.plot(x, y, 'ro')

        # If loop to check if self.collinear is True
        if self.max_points != None:

            # If loop to loop through each set of max points
            for i in self.max_points:

                # Plot a line between max points
                plt.plot([i[0][0],i[1][0]],[i[0][1],i[1][1]])

        # Save figure
        plt.savefig(f'{filename}')

        if self.show:
            plt.show()

        # Clear plot
        plt.cla()




