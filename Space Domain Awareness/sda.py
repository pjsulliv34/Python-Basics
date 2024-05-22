"""
This program reads in two input files that contain formatted satellite data. The read_telemetry function reads in the
satellite text file and creates a nested list containing the satellite country, altitude and velocity and closes the
text file. The check collision’s function reads in the nested satellite list and checks the list to see if any
satellites are at risk of colliding with each other. The final output is a printed message in the terminal and an alert
text file for each input file stating the countries at risk and not at risk of collision.
"""

# Main function which enables program to run only when ran via script, not when imported
def main():

    # Function for reading in satellite data
    def read_telemetry(file_name):

        # Opens text file
        with open(file_name) as reader:

            # Uses readline to get country count from first line in text file
            country_count = int(reader.readline().strip())

            # Initialize empty satellite list
            satellite_data = []

            # Loops through rest of file based on country count variable
            for item in range(country_count):

                # Read in country data
                line = reader.readline().strip().split(',')

                # Append satellite list with country data in correct format
                satellite_data.append([line[0], int(line[1]), float(line[2])])

            # Return country satellite nested list
            return satellite_data

    # Function to check nested satellite list for countrys at and not at risk of collision
    def check_collisions(satellites):

        # Initialize empty list
        collision_countries = []

        # For loop to loop through nested satellite list
        for country in satellites:

            # Initialize temp empty list
            collide_temp = []

            # For Loop to loop through satellite list again
            for other_county in satellites:

                # Checks if the current country in the first loop is the same in the nested loop
                if country[0] == other_county[0]:
                    continue

                # If clause to check if country is at risk of collision, if at risk, append to temp list
                if country[1] == other_county[1] and country[2] != other_county[2]:
                        collide_temp.append(other_county[0])

            # Append temp list of collisions to collision_countries list
            collision_countries.append([country[0],collide_temp])

        # Return the final nested collision countries list
        return collision_countries

    # List of input files for program in process
    input_files = ['satellites1-1.txt','satellites2-1.txt']

    # For loop that loops through indices of input files
    for file in range(len(input_files)):

        # Calls read telemetry function on input file
        satellite_data = read_telemetry(input_files[file])
        # Calls check collision on result from read telemtry function
        collided = check_collisions(satellite_data)

        # Creates an txt file for each input file
        f = open(f'satellites{file+1}_alerts.txt', 'w')
        print('')
        print(f'##### Space Command Simulation {file + 1} #####')

        # Writes message into txt file
        f.write(f'##### Space Command Simulation {file + 1} #####\n')

        # Loops through check collisions result
        for i in collided:

            # Checks to see if country collided with other countries. Prints and writes message based on if clause.
            if len(i[1])>0:
                print(f'{i[0]} is at risk of colliding with {i[1]}')
                f.write(f'{i[0]} is at risk of colliding with {i[1]}\n')
            else:
                print(f'{i[0]} is not at risk for a collision.')
                f.write(f'{i[0]} is not at risk for a collision.\n')

# Checks to see if dunder name changed to main
if __name__ == "__main__":
    main()


