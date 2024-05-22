"""
Prompts the user for a 15 digit incomplete credit card number.
Implements Luhn's Generation Algorithm working from the right to the left
of the credit card number. Generates the final digit that creates
a valid credit card number. Displays valid credit card number.
"""

# initial while loop is used to prompt the user for a 15 digit CC number
# if the length of the number is not 15, it will keep prompting.
# once we get 15 then the loop will break
while True:
    creditCardNumber = input('Please enter an identifier: ')
    if len(creditCardNumber) != 15:
        print('Identifier needs to be 15 digits')
    else:
        break


running_total = 0
counter = 0
# created a loop that loops through the range of -1 to the negative length of the credit card number
# at increments of -1. Needed the length to go to -15, so i subtracted 1 to make the range function go
# from -1 to -16
for i in range(-1, -len(creditCardNumber)-1, -1):
    counter += 1
    # if loop to check if the number is odd or even. Another if loop to check if the double of the even digits
    # are >10 or not
    if counter % 2 != 0:
        if int(creditCardNumber[i]) * 2 > 9:
            double_digit = str(int(creditCardNumber[i]) * 2)
            running_total += int(double_digit[0])+int(double_digit[1])
        else:
            running_total += int(creditCardNumber[i]) * 2
    else:
        running_total += int(creditCardNumber[i])

# Finally, we check to see what the final digit needs to be for the credit card number to be valid
# which means that the running total is divisible by 10 with the additional new number
finaldigit = 10 - (running_total % 10)
print(f'The valid credit card number is: {creditCardNumber+str(finaldigit)} and the newly computed'
      f' check digit is: {finaldigit}')
