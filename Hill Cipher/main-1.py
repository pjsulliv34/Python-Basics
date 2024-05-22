"""
This program creates three HillCipher objects.
If those objects are invertible, the function then encrypts the message using the key matrix and modulus. Then the
program takes that encrypted message and decrypts the message. To decrypt the message, the program calculates the
modular multiplicative inverse of the key matrix. Once we have the modular multiplicative inverse of the key matrix, the
program then uses that as the key to decrypt the encrypted message.
"""
# Import the Hillcipher class and numpy module
from hillcipher import Hillcipher
import numpy as np

# Create a main function to be called while running script
def main():

    # Create a mapping dictionary
    hill_cipher_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                       'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22,
                       'X': 23, 'Y': 24, 'Z': 25}

    # Create a variable called plain_text
    plain_text = 'ATTACKATDAWN'

    # Create a variable called mod
    mod = 26

    # 3 Key Matrices to Loop through in program
    key_matrix_1 = np.array([[19, 8, 4], [3, 12, 7]])
    key_matrix_2 = np.array([[7, 8], [11, 11]])
    key_matrix_3 = np.array([[5, 15], [4, 12]])

    # Creating 3 hillcipher ojbects
    hillcipher_object_1 = Hillcipher(plain_text, key_matrix_1, mod, hill_cipher_map)
    hillcipher_object_2 = Hillcipher(plain_text, key_matrix_2, mod, hill_cipher_map)
    hillcipher_object_3 = Hillcipher(plain_text, key_matrix_3, mod, hill_cipher_map)

    # Create a list containing the 3 hillcipher objects
    ciphers = [hillcipher_object_1,hillcipher_object_2,hillcipher_object_3]

    # For Loop to loop through ciphers
    for cipher in ciphers:

        # If clause to check if the matrix is invertible
        if cipher.invertible():

            print('The matrix is invertible\n')

            # Print Statement to print out cipher instance attribute
            print(f'Plaintext: {cipher.plaintext}')

            # Use cipher encode to print out encoded array of the cipher plaintext
            print(f'Plaintext column vectors: {cipher.encode(cipher.plaintext)}\n')

            # Initialize an empty encoded array
            encoded = []

            # Initialize an empty string encoded_text
            encoded_text = ''

            # For loop to loop through the encoded array using the plaintext to create the array
            for array in cipher.encode(cipher.plaintext):

                # Append encoded array with the encrypt numpy array
                encoded.append(cipher.encrypt(array))

                # Decode encrypted array and add to encoded text from the right
                encoded_text = encoded_text + cipher.decode(cipher.encrypt(array))

            # Print out encoded encoded text
            print(f'Ciphertext: {encoded_text}')

            # Print out encoded vector array
            print(f'Ciphertext column vectors: {encoded}\n')

            # Initialize empty string decoded
            decoded = ''

            # Inititalize empty list
            decoded_list = []

            # For loop to loop through encoded array
            for array in encoded:

                # Append decoded list with decrypted array
                decoded_list.append(cipher.decrypt(array))

                # Decode decrypted array and add to decoded string from the right
                decoded = decoded + cipher.decode(cipher.decrypt(array))

            # Print out decoded array list and decoded text
            print(f'Plaintext: {decoded}')
            print(f'Plaintext column vectors: {decoded_list}\n')

        else:
            # If clause to determine if the determinant is equal to 0
            if cipher.determinant() == 0:

                # Resulting print statement
                print('The determinant = 0.\n')

            elif cipher.key_matrix.shape[0] != cipher.key_matrix.shape[1]:

                # Resulting print statement
                print('The matrix is not square.\n')


# Checks to see if dunder name changed to main
if __name__ == "__main__":
    main()

