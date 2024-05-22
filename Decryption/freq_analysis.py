"""
This program reads in two files, a cipher text and a mapping file. We take the cipher text and perform a frequency
analysis on the cipher. We then use the mapping text to map out and convert the cipher to the decrypted message. The
message will only be roughly decrypted due to the fact that some letters have the same frequency shown in the mapping
file.
"""

# Main function which enables program to run only when ran via script, not when imported
def main():

    # Read in encrpyted message as a string
    def read_cipher(file):

        # opens text file in read mode
        with open(file,'r') as reader:

            # reads entire file
            message = reader.read()

        # Return string
        return message

    # Reads mapping file
    def read_mapping(file):

        # Initialize an empty dictionary
        frequency = {}

        #opens file in reader mode
        with open(file, 'r') as reader:

            # Creates a loop, that only breaks when a condition of false, or break statement
            while True:

                # read in line of text file
                line = reader.readline().strip()

                # If the line is blank, break while loop
                if line =='':
                    break
                # Special condition to handle blank space instead of integer, add to freq dictionary
                if line.split(':')[0] == '':
                    frequency[' '] = int(line.split(':')[1])
                # Add mapping to freq dictionary
                else:
                    frequency[line.split(':')[0]] = int(line.split(':')[1])
        # Return frequency dictionary
        return frequency

    # Get frequency count of cipher text
    def get_freq_counts(msg):

        # Initialize an empty dictionary
        count = {}

        # For slice in the string, calculate the number of times slice is in string and add that mapping to dictionary
        for i in msg:

            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        # Return frequency count dictionary
        return count

    # Read in cipher message from text file, return a string
    cipher_message = read_cipher('ciphertext.txt')

    # Read in string, return a dictionary with the frequency or each slice in the string
    cipher_frequency = get_freq_counts(cipher_message)

    # Read in text file with the frequency of each character in the decrypted message
    mapping_frequency = read_mapping('freq.txt')


    # Initialize an empty dicitonary
    new_mapping = {}

    # For loop to loop through the keys/values of the cipher frequency dictionary
    for key , value in cipher_frequency.items():

        # For loop to loop through keys/values of the mapping frequency dictionary
        for k , v in mapping_frequency.items():

            # If the value in the mapping equals value in cipher, then add new key value pair to new mapping
            if value == v:
                new_mapping[key] = k
                break

    # Initialize an empty string
    decrypted = ''

    # Loop through the original cipher message
    for i in range(len(cipher_message)):

        # For each character in the cipher message, add the new mapping value to the decrypted message
        decrypted = decrypted+new_mapping[cipher_message[i]]

    # Print out decrypted message
    print(f'\nDecryped Message: \n{decrypted}\n')

# Checks to see if dunder name changed to main
if __name__ == '__main__':
    main()



