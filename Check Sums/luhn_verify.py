"""
Prompts a user for two credit card numbers. For each credit card number,
the program implements Luhn's Verification Algorithm to check if the
credit card number is a valid credit card number.
"""

# initial for Loop to ask for the credit card number twice
for val in range(2):

    creditCardNumber = input('Please enter a credit card number: ')
    running_total = 0
    counter = 0

    # looping through the all numbers in the credit card, note the credit card number is a string to start
    for i in creditCardNumber:
        # initial counter is used to determine the even and odd place using the modulus
        counter += 1
        # if loop to check if the number is odd or even. Another if loop to check if the double of the even digits
        # are >10 or not
        if counter % 2 != 0:
            if int(i) * 2 > 9:
                double_digit = str(int(i) * 2)
                running_total += int(double_digit[0])+int(double_digit[1])
            else:
                running_total += int(i) * 2
        else:
            running_total += int(i)

    # Checksum is calculated using the modulus operator
    Checksum = running_total % 10
    print(f'Checksum = {Checksum}')

    # Next we have our final check, that looks at the check sum variable to determine if the credit
    # card number is valid or not.
    if Checksum == 0:
        print(f'{creditCardNumber} is a valid CC number.')
    else:
        print(f'{creditCardNumber} is an invalid CC number.')
