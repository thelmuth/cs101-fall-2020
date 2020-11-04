"""
Count the number of stars in an image of the night sky.
"""

import os
from PIL import Image

LUMINANCE_THRESHOLD = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    directory = os.getcwd()

    stars = Image.open(directory + "/stars1.jpg")
    
    make_stars_white_space_black(stars)
    
    stars.show()
    
    
    
    
def luminance(rgb):
    """Finds the average of r, g, and b components to determine how
    bright a pixel is."""
    
    (r, g, b) = rgb
    return (r + g + b) // 3
    
    
def make_stars_white_space_black(image):
    """Makes each pixel of a star white and of space black."""
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            lum = luminance(pixel)
            
            if lum < LUMINANCE_THRESHOLD:
                image.putpixel((x, y), BLACK)
            else:
                image.putpixel((x, y), WHITE)
                
    
            
            
            
            
            

if __name__ == "__main__":
    main()
    