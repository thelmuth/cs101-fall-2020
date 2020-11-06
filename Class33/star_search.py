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
    
#     stars.show()
    
    make_stars_white_space_black(stars)
    
#     stars.show()

    star_count = count_the_stars(stars)
    
#     turn_pixel_neighbors_black(stars, 38, 27)
    
    stars.show()
    
    print("the star count is", star_count)
    

def turn_pixel_neighbors_black(image, x, y):
    """Turns all neighbors of this (x,y) pixel black"""
    
    pixels_to_check = [(x, y)]
    
    while len(pixels_to_check) > 0:
        (x, y) = pixels_to_check.pop(0)
        
        pixel = image.getpixel((x, y))
        
        if pixel == WHITE:
            image.putpixel((x, y), BLACK)
            
            if x < image.width - 1:
                pixels_to_check.append((x+1, y))
            
            if x > 0:
                pixels_to_check.append((x-1, y))
                
            if y < image.height - 1:
                pixels_to_check.append((x, y+1))
                
            if y > 0:
                pixels_to_check.append((x, y-1))
    
    
def count_the_stars(image):
    """Count how many stars appear in the B&W image stars."""
    
    count = 0

    for y in range(image.height):
        print("y value is", y)
        for x in range(image.width):
            
            pixel = image.getpixel((x, y))
            
            if pixel == WHITE:
                turn_pixel_neighbors_black(image, x, y)
                count += 1
                
    return count
            
            
    
    
    
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
    