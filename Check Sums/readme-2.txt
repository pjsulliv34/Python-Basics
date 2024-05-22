Name: Peter Sullivan (psulli29)

Module Info: 

Module 3, Assignment 1. luhn_verify.py, luhn_generate.py
DueDate - 9/17/2023

Approach:

luhn_verify.py

For this problem, I first had to make sure that the user will get prompted to enter a credit card number twie. The problem required me to use a for loop to satisfy this. I looped through the range of 2. Which means it when from 0 and 1. This means the loop would run twice. Next I started building the logic of the problem inside the for loop. I prompted the user to input the credit card number. I then created two more variables, running total and counter and set those both to zero. Next I started looping through the string credit card number. Each time I went through the string, I incremented the counter by 1. I used the counter variable with the modulus operator to determine if the number is odd or even. If its even, then then counter % 2 should be zero. 

I then created an if clause to check if the number we are looking at is an even placed number or an odd placed number. I then created a new if clause to check if the number * 2 is larger then 9. To do this I needed to use the int function since the number was originally a string. If the double of the number is larger then 9, that means it has two digits and I need to add the sum of those digits to the running total. To do that, I created a new variable double_digit using the int function to allow me to multiply the number by 2. I turned double digit back into a string since this allows me to break out the digits of the variable to add them together. I then grab the first part of the string (double_digit) and turn it to an integer of the and add that to the second slice of the string in the same manner. If the digit *2 is not larger then 9, then I just add the digit multiplied by 2 to the running total using the int function and the multiply operator. If the counter is odd, then we just add the digit to the running total using the int function, since we are looking at a string.

Next I need to find the Checksum which tells me if the number is divisible by 10 or not. I used the running total variable and modulus operator to create the checksum variable. I then looked to see if the check sum is 0, if so, then the number is a valid CC number, otherwise the CC is invalid. I printed out the response for each using a print function, and a f string to print out the creditcardnumber variable.

luhn_generate.py

This problem is similar to the Luhn_verify.py. I first started the problem by creating a while loop. The problem states that we need to enter a 15 digit identifier. I created the while loop to check if the length of the number entered is not 15 using the len function. If the length is not 15, then we get a statement asking the user to enter a CC number. If the length is 15, then I use the break function to end the loop. Since I set the while loop to True as the start of the loop, the while loop will not end until we break out, since True is always true. As mentioned in the videos, the while loop looks for a Boolean response, true or false.

Next I create two variables set at zero, running total and counter. As mentioned above the counter is used with the modulus operator to determine the placement of the digit, odd or even.

Next we are asked to loop through the digits from right to left. In order to do this, I used a for loop and the range function. I set the initial step in the function to -1, the final step to the negative length of number minus 1. We had to add the minus one due to the way that the range function works. For example, range(1,3,1), will only print 1 and 2, excluding three at incrments at 1. Since we are moving backwards, we need the final digit of 15, so we have to go to -16. We also could have just put -16 there, since our while loop already determines that we only accept 15 digit codes. 

The if clauses in the for loop works exactly the same as mentioned in the luhn_verify.py.

Next we need to generate the new final digit. This is generated using the runningtotal variable and the modulus operator. 

Once we have the final digit, I then used the print function and an f string to print out the statement with the variables. I had to print out the final credit card number with the new final digit, which meant I had to add both strings together. The final digit was currently a int, so I used the str function on the finaldigit variable and then added them together with in the fstring to create the new credit card number in the print statement.

Known Bugs:
N/A
