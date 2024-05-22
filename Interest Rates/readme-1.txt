Name: Peter Sullivan (psulli29)

Module Info: 

Module 2, Assignment 1. interest.py, rate.py
DueDate - 9/10/2023

Approach:

interest.py

For this problem, I had to input four variables from the user: principle, rate, term and payments. These variables were then used in the total payout calculation. For this calculation, I had to use the +,* and** operators. I had first used int for all the variables when changing them over from a string. This caused an error in the code "invalid literal for int". This error was easily fixed by changing the type of the interest rate to float. I then used the print function and a f string to enter the variables into a string. The interest rate needed to be in percentage so I multiplied that by 100 in the fstring. I also needed to calculate the interest earned which is the (payout - principle), so I entered that in the f string as well instead of creating a new variable.


rate.py

For this problem, I had the user input four variables: principle, paid, term, and payments. These variables were then used to calculate the rate. To come up with the rate calcuation from the given equation, I first utilized the log and exp functions from the math package. After reviewing the office hour recording, I realized that we have not learned to import yet, so I had to solve this problem with out importing the math.log and math.exp functions. After a bit of trouble shooting my algebra, I realized that I could take the root of (term*payments) from both sides, to remove the exponent from the (1+rate/payments) on the right side. Once I did that, it only took basic algebra to seperate the rate from the other variables. The inputed varables had to be floats for both paid and principle. The rate equation took the inputed variables and calculated the rate. I finally used a print function with a fstring to input the variables and the calculated rate in percentage (rate *100) in the desired string statement that the problem stated.

Known Bugs:
N/A