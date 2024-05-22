Name: Peter Sullivan (psulli29)

Module Info: 

Module 5, Assignment 1. kmeans.py
DueDate - 10/01/23

Approach:

kmeans.py

I first created the input_files variable. This allowed me to loop through and print out the results for both texts files. I then used the with clause and open function, to open the text file in reader mode, declaring that file as the variable reader. I then used the readline function to read the first three lines of the file to gather the config info: iterations, total patients and cluster count. Declaring all three of those as variables. I then calculated the number of patients based on the total patients and cluster count variable.

I then needed to gather the centroid data. I created an empty list called centroids and gathered each centroids x and y components. The cluster count variable tells us how many clusters there are, which means how many centroids there are as well. Knowing that info, I created a for loop and used the range function to loop through the number of clusters and gather the centroid data in the text file. To do this, I first crated a variable called line using the readline() and strip() function. I then appended the centroids list with nested lists of x and y components of each centroid. To get the x and y component, i utilized the line variable and used the split function on the comma. This created two components of the variable the string before and after the comma. I then grabbed the correct index for the x and y component and converted it to a integer using the int function. Finally, I surrounded both the x and y component in brackets to turn this into a list, since I will need to modify it in the future. I then used the print function and an f string with triple quotes to print out the initial centroid data.

Next, I initialized an empty patients list. I then used a for loop and range function with the patients clustering list, to loop through the indices for the rest of the text file. If the text file is set up correctly, we should loop through the rest of the text file and get no errors. The patient data is in the same format as the centroid data, so I utilized the same method used to gather the patient x and y components. Create a line variable using reader, readline and strip variables. Append patient list with nested lists of x and y components of each patient utilizing the correct index of the split line variable on the comma and using a int function.

I then created an empty listed called clusters nested. Then I used a for loop, with the range function and the cluster count variable to append the clusters nested list with empty lists that correspond to the same number of clusters specified in the config details at the beginning of the text file.

We have successfully read in the file. Next, I created a variable called iter, that will measure the number iterations utilized in our program to achieve stability for the kmeans algorithm. I then created a for loop using the range function and the max number of iterations from the iterations variable. I then created an empty list called old cluster, this will be used to gather the previous iterations cluster group counts. To gather that info, I created a for loop using the range function and the cluster count variable. I then append the old cluster list with the length of each group using the len function. **note that the initial loop, the lengths will be 0 for each, since we have not grouped any patients. 
After I gather the cluster lengths, I then clear the clustered nested lists, using a for loop, range function and len function, and the clustered nested variable. **note that the lists are empty at first, so the clear function will make no difference on the first iteration. 

I then created a for loop to loop through all the patients using the range and len functions and the patients variable. 

I then created another for loop, with the range and len functions, but with the centroid list. This means for each patient we will loop again through the length of the centroids list. For each patient, I calculated the delta x and y variables, dx and dy. This is the distance from the patient x and y from each centroid. I then calculated the Euclidean distance using the dx and dy variables. Now that I had the distance, I needed to figure out which centroid the patient was closest too. To do this, I created an if clause, that creates two variables distance min and cluster min. For the first cluster, distance min is the current distance, and the cluster is the first cluster in the cluster group. Once we get past the first cluster, we then start checking the new distance calculated, if that distance is < then the current, we reset the distance min and cluster min variables.

After we loop through each cluster, I then set up another if clause that verifies that we are at the final cluster, and then appends the patient to the right cluster group based on the cluster min variable.

Now that the patients are correctly categorized, we now need to recalculate the centroids. I created a for loop using the range and len functions with the centroids list. I then initialized two empty x and y lists.

I then created a for loop using the range and len functions and the clusters nested lists to go through each group of patients, and append the x and y lists with the x and y component of each patient in the list. Once the x and y lists are set up for that cluster group. I then replace the x and y components of the centroid with the mean of the x and y for their group. I created the mean using the python built in function sum and the len function. After all the centroids have values have been modified, I then created an empty list called new cluster length. I then looped through the cluster count indices and appended the new cluster length list with the lengths of each new cluster group.

I then created an if clause to check that if the old cluster lengths equal the new cluster length. If so, we break the initial for loop that is used to loop through the range of the iterations variable, otherwise we add one to our iter variable and continue the for loop

If we do end up breaking, then we move down to the final print statements. I first use a print function with a f string to print out the total iterations needed. I then created two for loops to print out  the final centroid data, lengths of cluster groups and the final cluster groups as well using the print function and f strings and the corresponding variables.


Known Bugs:
If the text file is set up incorrectly, there are no safeguards to stop the program from running and incorrectly name config details. 

Citations:
Euclidean distance formula was obtained using last weeks hw. (Hw 4)

