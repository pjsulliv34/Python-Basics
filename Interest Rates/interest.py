"""
This code will calculate the Payout of a Certificate of Deposit based on the initial principle,
interest rate, the term of the CD in years, and the total number of interest payments per year.
"""
principle = int(input('Principle:  '))
interest_rate = float(input('Rate: '))
term = int(input('Term: '))
payments = int(input('Compound: '))

payout = principle*(1+interest_rate/payments)**(payments*term)

print(f'Investing ${principle} in a CD with an {interest_rate*100} interest rate for a term of {term} year(s)\nwill earn \
${(payout-principle)} in interest for a total payout of ${payout}')