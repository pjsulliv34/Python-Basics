Name: Peter Sullivan (psulli29)

Module Info: 

Module 14, point.py, collinear.py
DueDate - 12/12/2023

Approach:

point.py

In this program, I first import the pyplot package from matplotlib as plt. I first create a class called Point.

With in this class, I first use the init constructor to initialize the x_y_coord, max_points and show attributes. Max Points and show are defaulted to None and True respectively. 

Next, I create a method called Plot. Plot takes in the self keyword, a filename that will be a string. With in this function, I then initialize two lists, x and y. Then I loop through the X_y_coord attribute which is a list of data points. For each item in the list, I append the x list with the x coordinate and the y list with the y coordinate. I then use the matplotlib.plt.plot method to plot the x and y coordinates in red circles. 

Next, I create an if clause to check if the max_points attribute is not equal to None. If that is true, we then loop through the list of max points, each item should contain two points. For each Item, we then use the plot method again to plot a line between those points.

Next, we use the plt.savefig() method to save the plot in the current directory. This method uses the file name that was inputed when calling the Point.Plot() method. Next, we have another if clause to check if the show attribute was set to True, if so, then we show the plot using the plt.show() method.

Finally, we use the plt.cla() method to clear the plot. I needed to point this in due to issues with plotting multiple plots in a loop. I found my final plots had points from the other plots in the loop. So if I clear the loop, each time the plot is called, we can guarantee that it will be a clear graph to start with.


collinear.py

I first import the Point Class from point.py. Next, I created a class called Collinear. Next, I used the init constructor to initialize the filename attribute.

Next, I create a method called read_data which only takes in the self keyword. With in this method, I then use the with clause and the open function to read in the attribute filename as the variable reader. I then create a variable called number of points that reads in the first line of the txt file using the readline function and converts that line to an int using the int function.

I then initialize an empty list called data. I then use a for loop to loop through the range of the number of points variable. For each index, I then create a variable called line that reads in the current line of the txt using the readline() method and then splits the data into two parts using the split() function. I then use the append method to append the data list with a tuple containing two floats. To get each part, I use a slicer to indicate the first and second part of the line, and I use the float function to convert the str to float for each point. I append both parts as a tuple into the data list. I then return a list called data.

I then created a function called slope which takes in the self keyword, and two arguments, pair1 and pair2. These are each a list containing two items (x and y coordinates). I then use the try block to calculate the slope using the two pairs of points. If the block does not fail, I have an if clause to check if the slope is equal to -0.0, if so, I then change this to 0.0. The negative sign was causing issues when determining collinearity using the slopes. If the try block failed, I used an except block to check if the exception is a zero division error. If so, slope is set to 0. Finally, I would return the slope.

Next, I created a method called collinearity which takes in the self keyword and a number as an integer. With in this method, I first initialize a empty list called slopes. Next, I use the method read_data to create a list called points.

I then use a for loop to loop through the range of the len of the points list. With in this for loop, I then create an empty list called temp_slopes. I then create a second list to loop through the range of the current index of loop 1 +1, to the len(points list). This allows me to loop through every combination of indexes in the points list but without having duplicates. I then append the temp slopes list with a list containing three items [x coord, y coord, and the slope between x and y coord]. I calculate the slope using the slope method. Then when we are done looping through the inner for loop, I then append the slopes list with the temp_slopes. We go through every item in the first for loop. 

Next, I create an empty list called collinear and an index variable that is set to 0. I then create a for loop to loop through each line in the slopes list. With in this for loop, I then create an empty dictionary called temp dic. I then create another for loop to through each item in the line. I then use an if clause to check if the slope (third item) is in the dictionary, if so, add 1 to the value for that particular key. if not create a key value pair where the slope is the key and 1 is the value. 

Next, I have a for loop to loop through the keys/values of the temp_dic using the .items() method. With in that for loop, I then create an if clause to check if the value is equal to the num (entered when calling collinearity method) -1. This is minus one, since we are looking for 4 total points to match (if we are looking for 4). If I find 3 points that are colinear with one other point, that would give me three in the list, but 4 total points. If this is true, then we append the collinear list with a list containing the index and the key [index,slope]. We then increment the index by 1.

We then create a loop that loops through the collinear list. We then create an empty list called temp_lines. I then create an additional for loop to loop through the values in the slopes list but for the particular list item based on the index provided from the collinear list. I then use an if clause to check if the slope from the val in the slopes list is equal to the slope i the collinear list item. If so, I then append the templines list with the second item in val list. I then insert the first point into the index zero, since that point would be missing as we were looking at the points collinear to that particular point. Finally, I append lines list with the temp lines. And the loops will continue. At the end, we then return a list called lines that contains a list of lists that contain colinear points.

The next method I created is the most distant points which takes in the self key word and a list of points. This method will sort through all points and find the most distant two points using the Euclidean distance. To perform this, I first create an empty list called max_points. I then use a for loop to loop through each item in the list lines. I then create a variable called max_dist and set that to 0. Each item in lines is a list, so I create two nested for loops to loop through each pairing of points in the list. I used the same nested loop method explained in the collinearity method. I then calculate the distance from point one at index1 and point2 at index2 using the Euclidean distance formula. I then use an if clause to check if the distance is greater than the max distance, if so, I replace max dist with the new distance, and I set temp_max = [point1, point2]. After I loop through all points in the line, I append the max points list with the temp max. Finally, I return the max points list.

Next, I created a function called main that runs only when the script is run. With in this function, I first created a list called files, that contains all the points txt files that we will be looking at. I then create a for loop that loops through the range of length of the files list.

With in that for loop. I first create an object called colinear_ob using the Collinear class and inputting the txt file name. I then create a list called x_y_coords using the read data method on the collinear object. I then create a list called lines which contains all colinear points from the current txt file for the specified number of points. For this homework we specify 4, so I input 4 when colling the collinearity method on our colinear object.

I then added a print statement and printed out the txt file so that it would be easier to see the output. Next, I loop through the each line in the lines list using a for loop. For each line we need to print out the list without the square brackets. To remove the brackets, I first created an empty string called final. I created a for loop that loop through each character in the string version of the list. I then used an if clause to check if the character was a left or right square bracket, if not, then I would add the character to the right of the final string. After looping through all characters, I would then use a print statement with a f string to print out the message with the final variable.

Next I calculate the two most distant points for each of the items in the lines list. I do this using the most distant points method and passing in the lines nested list.

Next, I create a Point object called point_ob using the Point class. I pass in the x_y_coordinates list, and the most distant points list. Since I didn't pass in the True or false for the show argument, Show is automatically set to True and will display the plots when the plot method is called.

Next, I call the plot method on the point_ob and input a message using an f string.

Finally, I use an if function to check if the dunder name is equal to __main__. If that is the case then we run the main function. This clause will only be true if we run it via script.  

Known Bugs:
N/A

Citations:
https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html
https://www.cuemath.com/euclidean-distance-formula/
