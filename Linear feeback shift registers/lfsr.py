"""
This code creates a class called LFSR. LFSR stands for linear feedback shift register. This class takes an initial binary
number in string format and a number in integer format. The number (seed) and tap (number) are used to create an object
of the LFSR class. Using the XOR operator, we can random numbers using the initial binary seed and tap. The new binary
number in string format can be created by using the step() method in the LFSR class. The main function below is used to
demonstrate the new binary numbers created by using different seed and tap values.
"""

# Create class
class LFSR:

    # Create LFSR object with initial seed and tap values
    def __init__(self, seed: str, tap: int):

        # assigning instance variables
        self.seed = seed
        self.tap = tap

    # Create bit method
    def bit(self, i: int):
        # return the integer of the location of bit at index. LFSR's count index from right to left for tap value.
        return int(self.seed[-i])

    # Create step method
    def step(self):

        # XOR of far left bit of seed and the tap bit
        new_bit = int(self.seed[-len(self.seed)]) ^ self.bit(self.tap)

        # Reassign instance of seed to new seed value using the new bit generated using XOR
        self.seed = f'{self.seed[1:]}{new_bit}'

        # Return value of self.seed
        return self.seed

    # str constructor used to create a string representation of the LFSR object
    def __str__(self):

        # Returns the string representation of the seed when print is called.
        return  self.seed

# Create a main function to be called while running script
def main():

    # Creating lfsr objects
    lfsr1 = LFSR('0110100111', 2)
    lfsr2 = LFSR('0100110010', 8)
    lfsr3 = LFSR('1001011101', 5)
    lfsr4 = LFSR('0001001100', 1)
    lfsr5 = LFSR('1010011101', 7)

    # Calling the step method for each lfsr object and showing the new bit generated for each object
    print(f'{lfsr1.step()} {lfsr1.bit(-1)}\n')
    print(f'{lfsr2.step()} {lfsr2.bit(-1)}\n')
    print(f'{lfsr3.step()} {lfsr3.bit(-1)}\n')
    print(f'{lfsr4.step()} {lfsr4.bit(-1)}\n')
    print(f'{lfsr5.step()} {lfsr5.bit(-1)}\n')

# Checks to see if dunder name changed to main
if __name__ == '__main__':
    main()
