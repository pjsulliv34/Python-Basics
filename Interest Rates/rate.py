"""
This code will calculate the interest on a Certificate of Deposit based on the total principle amount,
the total amount paid from the CD, the term of the CD in years, and the number of interest payments per year.
"""
principle= float(input('Principle: '))
paid = float(input('Total: '))
term = int(input('Term: '))
payments= int(input('Compound: '))
rate = payments*((paid/principle)**(1/payments*term)-1)
print(f'The interest rate on a ${principle} CD \
that pays out ${paid} over \na {term} year term \
is {rate*100}%')

