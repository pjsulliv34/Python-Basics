"""
This program calls a recursive function called recursive_bbp. This recursive function takes an input integer, for this
particular task, the input has been hard coded to 10. For each iteration, the summation of the formula
Bailey-Borwein-Plouffe (BBP) is calculated. We keep iterating and summing until the final iteration of 0. Once we reach
the final iteration, the total summation is returned for the BBP formula.
"""

# Main function which enables program to run only when ran via script, not when imported
def main():

    # Import math module
    import math

    # Recursive function to perform recursive analysis
    def recursive_bbp(n):

        # Base case that allows function to end
        if n ==-1:
            return 0

        # Summation based on current n value, print result and current n value
        summation = (1/16**n)*(4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(8*n+6))
        print(f'{n}  {summation}')

        # Return the current summation, and calls function recursively
        return summation + recursive_bbp(n-1)

    # Print statement final output formatting
    print('')
    print(f'K Contribution to the value of π')

    # Call recursive function, hard coded to 10, sets to a variable
    BBP_value = recursive_bbp(10)

    # Print statements for final output
    print('')
    print(f'The BBP value of π = {BBP_value}')
    print(f'The math module value of π = {math.pi}')

# Checks to see if dunder name changed to main
if __name__ == "__main__":
    main()



