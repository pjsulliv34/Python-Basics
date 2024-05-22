"""
This program creates a class called ImageEncrypter. To develop an object from the class image encrypter, we use a
file name which should found in the same directory as the python program being run and an object from the LFSR class.
The image encrypter has many methods to help with modifying an object. To create these methods, this program utilizes
the PIL package. We can open the image using the open method. Load an image into a pixel access object using the
pixelate method (which are an easy way to modify an image). Encrypt the image using the encrypt method. And finally save
the image to the directory using the save_image method.

The current program is set that if one were to call the save_image
method, the program will open the image, load into a pixel access object, encrypt each pixel using the lfsr step method
and finally save that image in the current directory.
"""
# Import the Image module and LFSR Class
from lfsr import LFSR
from PIL import Image

# create a class
class ImageEncrypter:

    # Create an ImageEncrypter object with initial lfsr and filename values
    def __init__(self, lfsr, filename: str):

        # assigning instance variables
        self.lsfr = lfsr
        self.filename = filename

    # Create Open_image method
    def open_image(self):

        # create an image object using the Image module and open method
        image_object = Image.open(self.filename)

        # return the image object
        return image_object

    # Create a pixelate method
    def pixelate(self):

        # Call on open image method to create image object
        image = self.open_image()

        # create pixelated image access ojbect using image object
        pixelated = image.load()

        # Return pixel access object and image object
        return pixelated, image

    # Create encrypt method
    def encrypt(self):

        # create image pixel access object and image object using pixelate method
        pixel_access, image = self.pixelate()

        # create size tuple using size method
        size = image.size

        # For loop to loop through the range of x component of the size tuple
        for x in range(size[0]):
            # For loop to loop through the range of y component of the size tuple
            for y in range(size[1]):
                # Create an empty list
                temp_tup = []
                # For loop to loop through the range of tuple of RGB pixels
                for pixel in range(len((pixel_access[x,y]))):

                    # Create the encryption using the pixel value and the integer of the seed value, and XOR operator
                    encrypt = pixel_access[x,y][pixel] ^ int(self.lsfr.seed, 2)

                    # append encrypt pixel to temp list
                    temp_tup.append(encrypt)

                    # Call step method to create a new seed
                    self.lsfr.step()

                # After looping through all the pixels, modify the tuple of the pixel access object
                pixel_access[x, y] = tuple(temp_tup)

        # Return the modified image object
        return image

    # Create a save method
    def save_image(self, file_name: str):

        # Create an image using the encrypt method
        image = self.encrypt()

        # Save image to directory using filename
        image.save(file_name)

        # returns image
        return image

# Create a main function to be called while running script
def main():
    # Create image encrypter object using LRSR object and an image
    image_encrypter_object1 = ImageEncrypter(LFSR('10011010', 5), 'football.png')

    # Call save image method
    image1 = image_encrypter_object1.save_image('football_transform.png')

    # Call show method on the image object to display current image
    image1.show()

    # Create new image object using same LFSR object, but reading in encrypted image
    image_encrypter_object2 = ImageEncrypter(LFSR('10011010', 5), 'football_transform.png')

    # Call Save image method to encrypt the encrypted image
    image2 = image_encrypter_object2.save_image('football_transform_transform.png')

    # Call show method on the image object to display current image
    image2.show()

# Checks to see if dunder name changed to main
if __name__ == "__main__":
    main()

