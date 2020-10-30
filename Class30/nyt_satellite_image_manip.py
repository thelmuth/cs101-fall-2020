"""
Replicates some of the work of this NYT article.
https://www.nytimes.com/interactive/2020/09/02/upshot/america-political-spectrum.html

In particular, we can take an image, sort its pixels by luminance, and make the
new image.
"""

import os
from PIL import Image

def main():
    directory = os.getcwd()

    ### This is a satellite image of Blue Ridge, VA
    va = Image.open(directory + "/Blue_Ridge.jpg")
#     va.show()



    print(va.width)
    print(va.height)
    
    gradient = nyt(va)


def luminance(rgb):
    """Finds the average of r, g, and b components to determine how
    bright a pixel is."""
    
    (r, g, b) = rgb
    return (r + g + b) // 3


def nyt(image):
    """Replicates the NYT study cited in the docstring at the top."""

    ### Get all pixels into a list
    pixels = []
    
    for x in range(image.width):
        print("getting the pixel at x = ", x)
        
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            pixels.append(pixel)
            
    print(pixels[:10])
    
    ### We have the list of pixels, and we need to sort it by luminance.
    
    ### Create a new list that has a pixel's luminance stored with the pixel
    ### Each element of this list will look like (luminance, (r, g, b))
    ### Then, when we sort this list, it will sort on luminance, and when tied,
    ### will break the ties based on r (and then on g)
    
    pixels_with_luminance = []
    for pixel in pixels:
        lum = luminance(pixel)
        pwl = (lum, pixel)
        pixels_with_luminance.append(pwl)
    
    print("pixels with luminance:", pixels_with_luminance[:10])
    
    ### Now we can sort the pixels based on luminance:
    pixels_with_luminance.sort()
    print("pixels with luminance after sorting:", pixels_with_luminance[:10])
    
    
    


if __name__ == "__main__":
    main()
    