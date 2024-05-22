"""
This program runs a kmeans algorithm. The program reads in two different text files to show scalability to run on many
different files at once. The text files themselves contain config details in the first few lines, and covid-19 patient
details in the later lines. We first read in the config details from the text file. Then we load in the patient x,y
component details. For each patient we calculate the closest distance to the following centroid. Then we categorize
that patient based on the minimum distance. After categorizing every patient, we then recalculate the average x and y
component of each of the centroids based on the new groups. We then reiterate that process, regrouping based on the
centroids and minimum distance and recalculating the centroid x and y components. The process will break when we see
convergence. Convergence in this program will be achieved when the count of each group from the previous iteration
equals the count of the current iteration.

"""
# List that contains both input files
input_files = ['points1-1.txt','points2-1.txt']

# For loop to iterate between both text files
for file in input_files:

    # Opens up text file in read mode
    with open(file,'r') as reader:

        # Use readline to read first three lines.
        iterations = int(reader.readline().strip())
        total_patients= int(reader.readline().strip())
        cluster_count = int(reader.readline().strip())

        # Calculate the number of patients to cluster
        patients_clustering =total_patients-cluster_count

        # Initialize an empty cluster list
        centroids = []


        # Gather centroid x and y components, and add to cluster config
        for i in range(cluster_count):
            line = reader.readline().strip()
            centroids.append([int(line.split(',')[0]),int(line.split(',')[1])])

        # Print out initial covid patient centroids
        print(f"""  
Initial COVID-19 Patients: {centroids}""")

        # Initialize the patients list
        patients = []

        # Gather patient info and append to patient list in (x,y) format
        for i in range(patients_clustering):
            line = reader.readline().strip()
            patients.append([int(line.split(',')[0]), int(line.split(',')[1])])

        # Initialize the nested cluster list
        clusters_nested = []

        # Insert into the nested cluster list blank lists, one for each centroid
        for i in range(cluster_count):
            clusters_nested.append([])

    # Initialize iterations variable
    iter = 0

    # Start iterating through the kmeans algorithm
    for itereration in range(iterations):
        # Initialize an empty list for the old_cluster info
        old_cluster = []

        # For loop to gather the lengths of previous cluster groups, located in the nested cluster list
        for i in range(cluster_count):
            old_cluster.append(len(clusters_nested[i]))

        # For loop to empty the nested cluster lists
        for i in range(len(clusters_nested)):
            clusters_nested[i].clear()

        # This for loop is used to loop through every patient from the patients list
        for patient in range(len(patients)):

            # This for loop takes the current patient info and calculates the distance from each centroid
            for i in range(len(centroids)):

                # Calculate delta x and y components, and corresponding distance
                dx = centroids[i][0] - patients[patient][0]
                dy = centroids[i][1] - patients[patient][1]
                distance = (dx**2+dy**2)**(1/2)

                # Determine the cluster closest to patient and add that patient to the group
                if i == 0:
                    distance_min = distance
                    cluster_min = i
                else:
                    if distance < distance_min:
                        distance_min = distance
                        cluster_min = i
                if i == cluster_count-1:
                    clusters_nested[cluster_min].append(patients[patient])

        # Loop through indices of clusters
        for i in range(len(centroids)):

            # initialize empty x and y lists
            x_s = []
            y_s = []

            # For each cluster group add the x and y component of the patient to the blank list initialized above
            for patient in range(len(clusters_nested[i])):
                x_s.append(clusters_nested[i][patient][0])
                y_s.append(clusters_nested[i][patient][1])

            # Set each centroid with new x,y coordinates, x mean and y mean
            centroids[i][0] = sum(x_s)/len(x_s)
            centroids[i][1] = sum(y_s)/len(y_s)

        # Initialize empty cluster list
        new_cluster_length = []

        # Gather current length of each cluster group
        for i in range(cluster_count):
            new_cluster_length.append(len(clusters_nested[i]))

        # Check to see if previous cluster length equals current cluster lengths, for each group
        if old_cluster == new_cluster_length:
            break
        else:
            iter += 1

    # Print out cluster info in desired format
    print(f"""
Iterations to achieve stability: {iter}

Final Centroids:""")


    # Loop through and print out cluster info
    for i in range(cluster_count):
        print(centroids[i])
    for i in range(cluster_count):
        print(f"""
Number of patients in Cluster {i}: {len(clusters_nested[i])}
{clusters_nested[i]}""")
    print('')













