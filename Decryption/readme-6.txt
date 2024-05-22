Name: Peter Sullivan (psulli29)

Module Info: 

Midterm, Assignment 1. freq_analysis.py
DueDate - 10/14/23

Approach:

freq_analysis.py

For this program, I first created a function called main. This will enable the program to run only when run via script and not when imported. **note, the main method will be apart of an if clause at the bottom of the script. 

I created a function called read_cipher. This function will be used to read in the cipher message and return the message as a string. In the function I then use the with clause and open function to open the text file in reader mode, and I name that variable reader. I then use the read() function to read the entire text file and name it as a variable message. Finally, I returned the message variable.

I then created a function called read_mapping. This function reads in the freq.text file and returns a dictionary. With in this function, I first create an empty dictionary called frequency. I then open the text file in the same manner as the read cipher function. With the file open, I create a while loop, which will loop until a condition of false or a break statement. With in the while loop, I then create a variable called line, using the reader variable and the readline and strip functions. I then put an if clause to check if the line is blank, if so, then break and end the while loop. 

When looking at the freq.txt file, we can see that the key and value pairs are separated by a ":". In order to return the value of the left and right of the ":" for each line, I would use the spilt function based on the “:” and I would add the first part as a key and the second part as a value to the frequency dictionary.

I put an if clause to check if the key is blank, if so, add the key of one space instead of an empty string. I created this if clause, since it was returning an empty space at first instead of a full space. So when I decrypted the message It would return the words but they would all be together in one line. For example, "I am" would be "Iam". 

I then returned the frequency dictionary after going through each line.

I then created the function called get_freq_counts. This function takes in the message in which we read in using the read_cipher function. So the get freq counts function takes in a string, and returns the frequency count of each character in that string.

With in the get freq counts funciton I first initialize an empty dictionary called count. I then create a for loop that loops through the input string, one character at a time. I then use an if clause to check if the character does not exist in the dictionary count, if not in the dictionary, add the key with a value of one to the dictionary. If the key is in the dictionary, then add 1 to the value for that key. I then return the dictionary called count.

We now have all the functions needed to decrypt our message. I first use the read cipher function to read in the ciphertext file and returns a variable named cipher message. I then use the get_freq_counts function to read in the cipher message variable. This returns a dictionary named cipher_frequency. Next, I use the read_mapping function to read in the freq.txt file, to return another dictionary called mapping_frequency.

Next I create a empty dictionary called new_mapping. This will have the mapping from each character in the encrypted message to the decrypted character. I first create a for loop that loops through the keys, values of the cipher_frequency dictionary using the items method. I then used a nested for loop for the mapping_frequency using the same method. With in the nested for loop, I have an if clause to see if the cipher frequency value equals the mapping frequency value. If so, return the  key/value pair to the new_mapping dictionary. The key will be the key from the cipher frequency dictionary, and the value will be the key from the mapping frequency dictionary. Since we have duplicates values, I used a break clause to break the nested loop after we have a match as there is no need to loop through the entire nested loop if we already have our mapping.

We now have our new mapping showing how to convert each character from the encrypted cipher to the decrypted character. Next, we need to create the decrypted message using the new mapping.

I first create an empty string called decrypted. I then use a for loop with the range and len function using the cipher message variable. For each character in the cipher message, I take the current decrypted string and append that string with the value of the new mapping dictionary by using the cipher character as a key to the new_mapping dictionary.

I then print out the decrypted message using the print function and a f string. To get the desired formatting, I used the \n for spacing.
Finally, I use an if function to check if the dunder name is equal to __main__. If that is the case then we run the main function. This clause will only be true if we run it via script.
Here are my results.
Decrypted Message using freq_analysis.py:

mtcom thorn are the oss agents meeting in the rear of saint marys softh chfrch after rear agmiram smith retfrns from his trayem ayroag to mafritania for oyeration immicitscent

As we can see, the message is close, but there are some values that need to be changed. For example, m and l have the same frequency. y,v,b and p also have the same frequency. A couple other letters also have the same frequency. In order to get the MD5 hash to match, I had to slowly go through the message and change the characters to others that had the same frequency in the freq.text file. After going through the message, here is the final decrypted message.

Final Decrypted message:

ltcol thorn are the oss agents meeting in the rear of saint marys south church after rear admiral smith returns from his travel abroad to mauritania for operation illicitscent


Known Bugs:
N/A

Citations:
N/A
