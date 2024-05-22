"""
This program creates a class called HillCipher, that takes in a message as a string, a 2X2 matrix, a modulus and
a dictionary that maps out numbers to letters. The following methods are created determinant - returns the determinant
of the key matrix, invertible - checks to see if the key matrix is invertible, mod_inverse - returns the modular
multiplicative inverse, encode - encodes a string, decode - decodes an array and returns a string, encrypt - encrypts a
2x1 matrix using a key and text, get decryption key - returns decryption key matrix, and decrypt - decrypts a message
using the text and the decryption matrix.
"""
# Import the numpy module and name as np
import numpy as np

# Create the class HillCipher
class Hillcipher:

    # Create an HillCipher object with initial plaintext, key_matrix, modulus and mapping instances
    def __init__(self, plaintext: str, key_matrix, modulus: int, mapping):
        self.plaintext = plaintext
        self.key_matrix = key_matrix
        self.modulus = modulus
        self.mapping = mapping

    # Create the determinant method
    def determinant(self):

        # Calculating determinant by cross multiplying and subtracting matrix values
        determinant = self.key_matrix[0, 0] * self.key_matrix[1, 1] - self.key_matrix[0, 1]*self.key_matrix[1, 0]

        # Return determinant
        return determinant

    # Create the invertible method
    def invertible(self):

        # checks to see if the determinant does not equal zero and that the matrix is a square
        if self.determinant() != 0 and self.key_matrix.shape[0] == self.key_matrix.shape[1]:
            return True
        else:
            return False

    # Creates mod_inverse method
    def mod_inverse(self):

        # Creates a for loop to loop through range of modulus values
        for i in range(self.modulus):

            # calculation to check for modular inverse of n mod m
            if i * self.determinant() % self.modulus == 1:

                # Return mod_inverse
                return i

    # Creates encode method
    def encode(self, string: str):

        # Initialize an encoded_string and temp_array list
        encoded_array = []
        temp_array = []

        # For loop to loop through each character in string
        for char in string:
            # Grabs numeric value based on dictionary and appends to temp_array list as a list
            temp_array.append([self.mapping.get(char)])

            # If clause to check if the temp array list is a length of 2, if so then add to encoded list as an array
            if len(temp_array) == 2:

                # Add temp array to encoded string list
                encoded_array.append(np.array(temp_array))

                # Clear temp array for next set of two characters
                temp_array = []

        # Returns encoded string list
        return encoded_array

    # Creates decode method that takes in a 2X1 array
    def decode(self, encoded_array):

        # Initialize an empty string
        decoded = ''

        # For loop to loop through encoded array
        for item in encoded_array:

            # For loop to loop through the mapping dictionary
            for key, value in self.mapping.items():

                # If clause to check if the value in the dictionary equals encoded array value
                if value == item:

                    # Grabs index value and adds to decoded string
                    decoded = decoded + key

        # Returns decoded string
        return decoded

    # Creates encrypt method
    def encrypt(self,encoded_array):

        # Returns the dot product of the key matrix and encoded array mod the mod value
        return np.dot(self.key_matrix, encoded_array) % self.modulus

    # Create get_decription key method
    def get_decryption_key(self):

        # Grabs the inverse determinant using the mod inverse method
        inverse_determinant = self.mod_inverse()

        # Creates the mod matrix that will be multiplied by the inverse determinant
        mod_matrix = np.array([[self.key_matrix[1][1], -self.key_matrix[0][1]], [-self.key_matrix[1][0] , self.key_matrix[0][0]]])

        # Return inverse key matrix
        return (inverse_determinant * (mod_matrix % self.modulus)) % self.modulus

    # Create the decrypt method
    def decrypt(self, encrypt_matrix):

        # Grabs the Inverse key matrix using the get descryption key method
        decrypt_key = self.get_decryption_key()

        # Returns dot product of the key matrix and encoded array mod the mod value
        return np.dot(decrypt_key, encrypt_matrix) % self.modulus

