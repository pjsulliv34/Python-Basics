"""
This program loops through 4 different txt files that contain point (x/y) data in string form. The program first creates
a collinear object using the name of the txt file. The program then gathers the x/y coordinates using the read_data
method. The program then determines any lines of collinearity using the collinearity function with a specified number
of points. The file then loops through each line of collinear points and creates a string representation stripping
the square brackets from the list and printing out that string. The program then calculates the most distant points
for each line of colinear points. Finally, we create a Point object called plot using the Point class, using the xy
coordinates and the most distant points. Since we did not specify the show, the show will be set True. We then use
the plot method specifying the name of the plot object.
"""
# Import point class from point.py
from point import Point

# Create class collinear
class Collinear:

    # Create a Collinear object with initial filename instance
    def __init__(self, filename):
        self.filename = filename

    # Create read_data method
    def read_data(self):

        # Opens Text File
        with open(self.filename) as reader:

            # Read in number of points from first line of file
            number_of_points = int(reader.readline())

            # Initialize empty data list
            data = []

            # For loop to through range of number of points variable
            for i in range(number_of_points):

                # Read in line of text file
                line = reader.readline().split()

                # Append data list with x and y coordinates
                data.append((float(line[0]), float(line[1])))

        # Return x/y coordinate list
        return data

    # Create the Slope method
    def slope(self, pair1, pair2):

        # Try/except to calculate slope based on two points
        try:

            # Calculate slope using x/y coordinates of two points
            slope = (pair2[1] - pair1[1]) / (pair2[0] - pair1[0])

            # If clause to check if any value is -0.0
            if slope == -0.0:
                slope = 0.0

        # Except clause for dealing with Zerodivision error
        except ZeroDivisionError:
            slope = 0.0

        # Return the slope value a float
        return slope

    # Create method Collinearity
    def collinearity(self, num: int):

        # Initialize empty list
        slopes = []

        # Read in the data from text file using read_data method
        points = self.read_data()

        # Loop through the range of the points list
        for index1 in range(len(points)):

            # Initialize empty list
            temp_slopes = []

            # Loop through points list again, but always starting one to right of the index1 loop
            for index2 in range(index1 + 1, len(points)):

                # Append the temp slopes with a list containing the points and the slope of the points
                temp_slopes.append([points[index1], points[index2], self.slope(points[index1], points[index2])])

            # Append the slopes list with the temp slopes
            slopes.append(temp_slopes)

        # Initialize an empty list
        collinear = []

        # Initialize index variable at zero
        index = 0

        # For loop to loop through each set of points/slopes
        for line in slopes:

            # Initialize an empty dictionary
            temp_dic = {}

            # For loop to loop through each pair of data points
            for pair in line:

                # If clause to check if slope value in dictionary
                if pair[2] in temp_dic:

                    # Add 1 to the value in the dictionary pair
                    temp_dic[pair[2]] += 1

                else:

                    # Create key/value pair for slope in temp_dic
                    temp_dic[pair[2]] = 1

            # For loop to loop through key/values in items
            for key, val in temp_dic.items():

                # If clause to check if the val == num -1
                if val == num-1:

                    # Append collinear list with index and key
                    collinear.append([index, key])
            # Increment index by 1
            index += 1

        # Initialize empty list
        lines = []



        # For loop to loop through collinear list
        for i in collinear:

            # Initialize empty list
            temp_lines = []

            # For loop to loop through
            for val in slopes[i[0]]:

                # If clause to check if slope equals the slope in collinear
                if val[2] == i[1]:

                    # Append the temp lines list
                    temp_lines.append(val[1])

            # Insert the original starting point at first index in the temp list
            temp_lines.insert(0, val[0])

            # Append lines list with temp lines list
            lines.append(temp_lines)



        # Return the lines list
        return lines

    # Create the most_distant_points method
    def most_distant_points(self, line):

        # Initialize empty list
        max_points = []

        # Loop through each line in the line list
        for i in line:

            # Initialize max_dist variable with reference to zero
            max_dist = 0

            # For loop to loop through range of the line
            for index1 in range(len(i)):

                # Loop through line list again, but always starting one to right of the index1 loop
                for index2 in range(index1 + 1, len(i)):

                    # Calculate the Euclidean distance between two points
                    distance = ((i[index2][0] - i[index1][0]) ** 2 \
                                + (i[index2][1] - i[index1][1]) ** 2) ** (1 / 2)

                    # If clause to check if the distance is larger than the max
                    if distance > max_dist:

                        # Reassign max_ditance and create temp max data point pair
                        max_dist = distance
                        temp_max = [i[index1], i[index2]]

            # Append maxpoints list with the temp max
            max_points.append(temp_max)

        # Return the max points lists
        return max_points

# Main function which enables program to run only when ran via script, not when imported
def main():

    # List of points file for the programs to process
    files = ['points1.txt', 'points2.txt', 'points3.txt', 'points4.txt']

    # For loop to loop through the length of the files list
    for i in range(len(files)):

        # Crreate a Collinear object using the file name
        colinear_ob = Collinear(files[i])

        # Read in the point data using the read data method
        x_y_coords = colinear_ob.read_data()

        # Determine any lines of collinearity with the length of 4
        lines = colinear_ob.collinearity(4)

        # Print Statement to show index of file being printed
        print(f'\n{files[i]}')

        # For loop to loop through each of the collinear lines
        for line in lines:

            # Initialize an empty string
            final = ''

            # For loop to loop through the str representation of the line
            for char in str(line):

                # If clause to remove square brackets from line string
                if char not in ["[","]"]:

                    # Append final string with character from the right
                    final = final+char

            # Print out the string representation of the line
            print(f'Line: {final}')

        # Calculate the most distant points for each line
        most_distant = colinear_ob.most_distant_points(lines)

        # Create the Point object
        point_ob = Point(x_y_coords, most_distant)

        # Plot and save object using the Point.plot method
        point_ob.plot(f'Collinear Plot {files[i][:7]}')

# Checks to see if dunder name changed to main
if __name__ == "__main__":
    main()