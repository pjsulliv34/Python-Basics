Name: Peter Sullivan (psulli29)

Module Info: 

Module 6, Assignment 1. sda.py, Assigment 2. bbp.py
DueDate - 10/08/23

Approach:

sda.py

For this program, I first created a function called main. This will enable the program to run only when run via script and not when imported. **note, the main method will be apart of a if clause at the bottom of the script. 

I then created a function called read_telemetry using the def clause. This function will take in a file name. I then use the with clause and open function to name a variable called reader. I then read the first line using the readline function, and strip() function. Since this is a number I also use the int function to convert it from string to integer and name the variable country count.

I then initialize an empty list called satellite data. Next, I use a for loop and range function to loop through the length based on the country count variable. For each index I read the first line using the readline, strip and split function based on commas. I then append the satellite data list with a nested list containing all three elements of the line. The country, altitude and velocity. Finally, I return the satellite data nested list.

The next function I created is called check collisions. I created the function using def clause. This function takes in a list. Inside that function I first initialized an empty list called collision countries. Next, I created a for loop, for which I looped through the input list. Inside that for loop, I then create an empty list called collide_temp. This is a temporary list since it will be recreated for every item in the loop as an empty list. I then create another for loop where I loop through the input list again. This allows me to go through every combination of two countries. 

Next, I have an if clause that checks if the country from the outer loop is equal to the country from the inner loop. If that is the case, then we use the continue statement to continue to the next loop in the for loop. If that is not the case, we then move to the next if clause, where we check if each country’s altitude is the same, and if so, whether the velocities are not equal. If both of these conditions are fulfilled, we then add this country to the temp list. We then loop through the rest of the inner loop. Once we have looped through the inner loop, we append the collision countries list with the country name, and the countries that it will collide with as a nested loop. We do this for every country in the outer loop. ** note that if there are no countries that collide with the country, the country will have an empty list appended with its name to the collision countries list. We then return the nested list called collision countries.

Next, we a have a list called input files that contains the names of the files that contain the satellite data.

I then created a for loop using the range and len function to loop through the indices of the input files list. I then use the read telemetry function to read each item in the input files list and name the output as satellite data. I then use the check collision function to read the satellite data variable and the output is used to create the variable called collided.

I now have a list of countries and the countries that each country will collide with, if they are going to collide. 

Next, I use the open function to create a variable called f. I used the 'w' argument, since we have not created a text file yet. I then print out the current simulation using a print function and the fstring. Next, I use the write function to write to the variable f, which is used for our txt file.

I then create a for loop to loop through the collided variable. I use a len function to check the second argument in the nested list for each item. If the second index of each list is greater then 1, then that country will collide with other countries. If that is the case, we print out a response to the console using the print funciton and the fstring. We also write the response to the txt file using the f variable and write function. If that is not the case, we then print to the console in the same manner and write to the txt file, but use a different message.

Finally, I use an if function to check if the dunder name is equal to __main__. If that is the case then we run the main function. This clause will only be true if we run it via script.

bbp.py

For this program, I first created a function called main. This will enable the program to run only when run via script and not when imported. **note, the main method will be a part of an if clause at the bottom of the script.

I then use the import function to import the math module. Next, I use the def clause to create a function called recursive_bbp. This function takes in an integer. I then created a base case that checks if the integer is equal to -1 using an if clause. If that is the case, the function returns 0.

If we don't have the base case, then I create a summation variable based on current n value using the Bailey-Borwein-Plouffe (BBP) formula. I then use a print function and an fstring to print out the current n value and the summation variable. 

Finally, I return the summation variable + the recursive_bbp(n-1). Which means I return the summation variable and add it to the call of function again, but 1 less then the previous n value. This function will keep calling itself until the base case if clause is met.

Next, I use a print function to print out desired formatting and text. I then create a variable called BPP_value, which calls the recursive function using a value of 10 for n. I hard coded the function to 10 since the hw is asking for a value of 10 for n. 

I then use the print function and a fstring to print out the BBP value and the math.pi value.

Finally, I use an if function to check if the dunder name is equal to __main__. If that is the case then we run the main function. This clause will only be true if we run it via script.




Known Bugs:
N/A

Citations:
Bailey-Borwein-Plouffe (BBP) formula, provided in the hw pdf.

