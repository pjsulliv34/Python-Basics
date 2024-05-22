Name: Peter Sullivan (psulli29)

Module Info: 

Module 11, Assignment 1. hillcipher.py
DueDate - 11/12/2023

Approach:

hillcipher.py

For this program I first imported the numpy module as np to allow for an easier call of the numpy class when calling numpy methods. Next, I created the class Hillcipher. Next, I use the init constructor which takes the self keyword, plaintext as a string, key_matrix as a matrix, modulus as an int and mapping as a dictionary. I then assign the instance variables to the plaintext, keymatrix, modulus and mapping respectively.

Next, I create the method called determinant which takes only the self keyword. For this class we are only using 2/2 matrices to calculate the determinant, so I manually calculated the determinant by cross multiplying and subtracting the values in the key matrix. If we were to use larger square matrices, we would need to update the code to use the numpy.linalg.det method, but the professor stated that we can manually calculate the determinant. The method then returns the determinant.

The next method I created is the invertible method that takes only the self keyword. With in the method, I create an if clause to check if the determinant is not equal to 0 and the shape of the matrix is a square. If yes, return True, otherwise return false.

The next method I created is the mod_inverse method which takes only the self keyword. With in the method I create a for loop to loop through the range of the modulus. Using the youtube video provided below in the citations, we know that the modulus modular multiplicative inverse of n mod m is in the range of 1 - mod value. So, we only need to loop through the total range of the mod provided. With in the for loop I then checked to see if the value in the loop multiplied by the determinant mod the mod value equals one. If so, return that value of modular multiplicative inverse in the loop. Otherwise continue the for loop and check the equation again. Finally, we return the integer value for the mod_inverse.

The method I created is the encode method, which takes the self keyword and a string. With in this method, I first created two empty lists, encoded array and temp array. I then created a for loop to loop through the string, for each character in the string, I use the get method to grab the corresponding value provided in our mapping dictionary and append to the temp array as a list of one. I then created an if clause to check if the length of the array is equal to 2, if so, I append the temp array list of 2 single list numbers to the encoded array list, I also change the temp_array to an array using the numpy array method. I then clear the temp array list and the for loop continues. Finally, I return encoded array list.

The next method I created is the decode method, which takes in the self keyword and an encoded array, and expects a 2X1 matrix. With in this method, I first create an empty string called decoded. I then loop through a 2 X 1 matrix, grabbing each value. I then created another for loop to loop through the keys and values in the mapping dictionary using the items method. With in that for loop, I check to see if the value of dictionary is equal to the value in the 2X1 matrix, if so, I add the key of that value to the decoded string from the right. Then the method returns the decoded string. We are expecting this return a string of length two, assuming that each character is in the dictionary.

The next method is the encrypt method, which takes in the self keyword and an array. The method then returns the modulus of the dot product of the key matrix and the encoded array. This method expects a 2X1 matrix as the input for the input array and returns an encrypted 2X1 matrix.

The next method is the get description key method, which only uses the self keyword. With in this method, I first create a variable called inverse determinant using the mod inverse method. I then need to create mod_matrix that I will use to multiply against the inverse determinant. Using the key matrix, I swapped the 0,0 and 1,1 positions and swapped the signs on the 0,1 and 1,0 positions. Finally, I returned the mod of the inverse multiplied by the mod of the mod matrix. This calculation gives us our inverse key matrix, that will be used to decrypt the 2x1 matrices.

The next method created is the decrypt method which takes in the self keyword and a 2x1 encrypted matrix. We then use the get decryption key method get the decrypt matrix to create the variable called decrypt key. I then return the modulus of the dot product of the decrypt matrix and the encrypt matrix, which will be a 2x1 matrix.


main.py

First I import the Hillcipher class from hillcipher.py. I also import the numpy module as np.

Next I create a function called main, which will be called only when running this script. With in this function, I create a dictionary called hill cipher map, a variable called plaintext which is a string, and a variable called mod which is a integer. I then created three matrices using the numpy array method using the values that were provided in the homework. I then created three Hillcipher objects using the Hillcipher class and the following variable, plaintext, key matrix, mod and hill cipher mapping. I then created a list called ciphers containing all our objects.

Next I created a for loop to loop through the cipher objects. With in the for loop, I created an if clause to check if the matrix is Invertible using the invertible method. If the matrix is invertible, I then print that the matrix is invertible. I then use the print function to also print the plaintext instance attribute of the current cipher object using a f string. I then use the print function and a fstring  to print out the array version of the encoded plain text, using the instance attribute plaintext and the encode method.

I then initialized an empty string and list called encoded text and encoded. I then used a for loop to loop through each array in the list of arrays returned by using the encode method with the plaintext instance attribute. For each array, I append the encoded list with the encrypted array (2X1) which is created by calling the encrypt method. I then use the decode method on the encrypted array to add to the encoded text from the right of the string. Once the for loop is done, I then use to print function, to print out the encoded text and the list of encoded arrays.

Next, I initialized an empty string called decoded, and an empty list called decoded list. I then created a for loop to through each 2x1 matrix. I then append the decoded list with an decrypted array using the decrypt method. I also decrypted the array using the decrypt method, and then decoded the array to a string, and then added that string to the decoded string from the right.

Next I utilized the print function with an f string to print out the decoded list and the decoded string.

If the cipher is not invertible, I then would go to an if clause that would check if the determinant is equal to zero, if so then the resulting print statement, if not, it would then check again to see if the shape components in the x and y are not equal. If so, then it would print the following print statement.

Finally, I use an if function to check if the dunder name is equal to __main__. If that is the case then we run the main function. This clause will only be true if we run it via script.

Known Bugs:
The get descryption key and determinant methods are hard coded to work on a 2X2 key matrix. For larger matrices, the code will need to be modified.

Citations:

https://www.youtube.com/watch?v=_bRVA5b4sb4
