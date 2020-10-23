import os
from PIL import Image

def main():

    directory = os.getcwd()
    
    #print(directory)
    
    ### Opens the image from the current working directory
#     kids = Image.open(directory + "/box_big.jpg")
    kids = Image.open(directory + "/box.jpg")
    
#     kids.show()

    ### Print some info about the image
    ### These are not method calls; they do not have parentheses
    print("width", kids.width)
    print("height", kids.height)
    
    ### What is the color at pixel (2000, 1600)?
#     print(kids.getpixel((2000, 1600)))
    
    ### Let's change this pixel to black
#     kids.putpixel((2000, 1600), (0,0,0))
    kids.show()
    
    ### Let's write a function to make an image more blue
    blue_filter(kids)
    kids.show()
    
    ### Turns out, we can have RGB values outside of [0, 255]. But,
    ### they are just adjusted to 255 if they are > 255, and adjusted
    ### to 0 if they are < 0.
    
    ### Why didn't we return an image?
    ### The function made changes to the image object, not a copy.
    ### This mutated the original image, which we can then see in the
    ### main function. Mutated objects don't have to be returned.

    ### To save the image
    kids.save(directory + "/kids_blue.jpg")


def blue_filter(image):
    """Takes an image and makes it more blue.
    This is a good template for all useful image functions!"""
    
    for x in range(image.width):
        print(x)
        
        for y in range(image.height):
            (r,g,b) = image.getpixel((x, y))
            
            image.putpixel((x, y), (r, g, b + 100))
            
#             if b > 200:
#                 print(b)
    

if __name__ == "__main__":
    main()
    