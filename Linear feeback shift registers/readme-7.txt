Name: Peter Sullivan (psulli29)

Module Info: 

Module 8, Assignment 1. lfsr.py, image_encrypter.py
DueDate - 10/28/23

Approach:

lfsr.py

In this program I first created a class called LFSR using the class keyword. Next, I use the init constructor which takes the self keyword, seed as a string and tap as an integer. With in the init constructor, I then assign instance variables to the seed and tap.

I then created a method called bit. This method takes the self keyword and an int variable called i. This method returns the integer of the - index of the i value inputted of the instance variable of seed. I used the negative index, since the LFSR algorithm counts from right to left when assigning tap values.

Next, I created a method called step which only takes in the self key word. With in this method, I first create a variable called new_bit. New_bit is the result of XOR'ing the far left bit and the tap value. To get the far left bit, I sliced the string of the seed value to the far left index using the negative len of the seed string. I then turned it into an integer. To get the tap bit, I called the bit method, and used the instance of tap as the input variable.

Next, I needed to reassign the instance of seed to the new random bit. To do this I used an f string, that popped off the far left character using slicing and added the new bit to the right of the string. I then returned the instance of the seed value.

Next, I created a method using the str constructor. This constructor is used to create a string representation of the LFSR object. With in this method, I return the string that I would like shown when calling print on my lfsr object.

I then created a main function that would be used when running this script. With in this main function, I created 5 different lfsr objects with the bit and tap values requested in the homework.

I then used a print function with an f string to show the new bit created when calling the step method on each of the 5 objects created. next to this string, I also included the new bit that was created by calling the bit method and requesting the far right index, which is the new bit that was appended to the seed from the right. At the end of the f string I included the \n to create a space after each print call.

Finally, I use an if function to check if the dunder name is equal to __main__. If that is the case then we run the main function. This clause will only be true if we run it via script.



image_encrypter.py

For this program, I first imported the LFSR class from the lfsr.py that I created earlier. I also imported the Image module from PIL (python imaging library). The PIL.Image is cited down below in citations.

I then created a class called ImageEncrypter using the class keyword. I then use the init constructor to create an ImageEncrypter object with the initial instances lfsr and filename values. With in the method, I then assign the instance variables the values that were inputted when creating the object.

Next, I created a method called open_image which takes in only the self keyword. With in this method, I then create a variable called image_object which uses the method open from the Image class calling the instance of filename. This method returns the image_object.

I then created a method called pixelate which only takes in the self keyword. This method first creates an image object by calling the open_image method. I then create a pixel access object using the load method from the Image class. I then return the pixel access object and the image object.

Next I create a method called encrypt which only takes in the self keyword. I first create the pixel access and image objects by calling the pixelate method. Next, I create a tuple by calling the size method on the image object. This gives the x, and y lengths of the pixel access matrix.

Using the size variable, I use two for loops, one looping through the x component and one looping through the y component. This allows me to loop through every single pixel in the pixel access object. With in the second nested for loop, I create an empty list called temp_tup. Next I create a final for loop that loops through the range of the len of the current tuple of RGP pixels based on the x and y locations of the pixel access object from the for loops. For each pixel I create a variable called encrypt which takes the XOR of the pixel and the current seed value from the lfsr value. To grab the seed value I used the dot operator to grab the current instance of seed. This is a string, and I need to convert it to a integer for the XOR operation. To convert it to an integer, I use the int function, and I add 2 as the second input in the function which tells the int function that I want base 2 instead of the default of base 10. I then append the temp tup list with the encrypted pixel. I then called the step method for my lfsr object. This creates a new seed value. We then perform the process for all pixels in the rgb tupple.

After I've looped through all pixels in the tuple, I then replace the current pixel in the pixel access object based on the x and y variable from the for loop with the tuple of the temp_tup list. The temp tup list will reference an empty list before we loop through the pixels. We perform this process for every single combination of x and y in the for loops. Which allows us to modify every single pixel in the pixel access object. 

Finally, I return the image object. Note** there is no need to return the pixel access object, as the image object itself was modified using the pixel access object.

The next method I created is the save_image method. This method takes in the self keyword, and a file_name variable (which should be a string). With in this method we first call the encrypt method to create an image object. I then take that image and use the save method with the filename input. I then return the encrypted image.

Next I create a function called main, which will be called only when running this script. With in this function, I first create an ImageEncrypter object using a LFSR object and the filename (football.png) as a string and name the object image_encrypter_object1. The LFSR object is created using the LFSR class, and the binary number as a string and a tap value as an integer. To encrypt and save the image as the encrypted image, I then took that Image Encrypter object and called the save_image method using the input of the desired filename (football_transform.png). I create a variable called image1 using the save_image method. Using this image1 variable, I then called the show method will allow python to display the encrypted image.

Next I create another Image Encrypter Object called image_encrypter_object2 using the same lfsr object, but a different file name (football_transform.png). This is the encrypted file name that was created using the first image encrypter object from above. I then use the save_image method with the file name football_transform_transform.png. I used the save method to create the variable called image2. Using this image2 variable, I then called the show method will allow python to display the encrypted image from the save_message method.

Finally, I use an if function to check if the dunder name is equal to __main__. If that is the case then we run the main function. This clause will only be true if we run it via script.


Known Bugs:
N/A

Citations:

https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image