import os
from PIL import Image

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():

    directory = os.getcwd()
    
    ### Opens the image from the current working directory
    kids = Image.open(directory + "/box.jpg")
    kids.show()
    
    ### Let's write a function to make an image more blue
#     blue_filter(kids)
#     kids.show()
    
    ### Let's make a function that will change an image into black and white
#     black_and_white(kids)
#     kids.show()

    ### Detect the edges
    edge_detect(kids, 20)
    kids.show()


def luminance(rgb):
    """Finds the average of r, g, and b components to determine how
    bright a pixel is."""
    
    (r, g, b) = rgb
    return (r + g + b) // 3


def edge_detect(image, luminance_threshold):
    """Finds the edges of objects in an image, and returns a B&W version
    where the edges of objects are black and non-edges are white.
    luminance_threshold is the difference in luminance at which to call
    two pixels different."""
    
    for x in range(image.width - 1):
        print(x)
        
        for y in range(image.height - 1):
            
            ### We need to get the RGB of the pixel and its neighbors
            pixel = image.getpixel((x, y))
            pixel_right = image.getpixel((x + 1, y))
            pixel_down = image.getpixel((x, y + 1))
            
            ### Get the luminance (avg. of R, G, and B) of pixel and neighbors
            lum_pixel = luminance(pixel)
            lum_right = luminance(pixel_right)
            lum_down  = luminance(pixel_down)
            
            ### is the difference between the pixel and a neighbor
            ### greater than the threshold?
            if abs(lum_pixel - lum_right) > luminance_threshold:
                image.putpixel((x, y), BLACK)
            elif abs(lum_pixel - lum_down) > luminance_threshold:
                image.putpixel((x, y), BLACK)
            else:
                image.putpixel((x, y), WHITE)
                
    
    
def black_and_white(image):
    """Takes an image and makes it black and white."""
    
    for x in range(image.width):
        print(x)
        
        for y in range(image.height):
            rgb = image.getpixel((x, y))
            
            avg = luminance(rgb)
            
            if avg < 128:
                image.putpixel((x, y), BLACK)
            else:
                image.putpixel((x, y), (255, 255, 255))

#             if avg < 85:
#                 image.putpixel((x, y), (0, 0, 0))
#             elif avg < 170:
#                 image.putpixel((x, y), (128, 128, 128))
#             else:
#                 image.putpixel((x, y), (255, 255, 255))
                

def blue_filter(image):
    """Takes an image and makes it more blue.
    This is a good template for all useful image functions!"""
    
    for x in range(image.width):
        print(x)
        
        for y in range(image.height):
            (r,g,b) = image.getpixel((x, y))
            
            image.putpixel((x, y), (r, g, b + 100))
            
    

if __name__ == "__main__":
    main()
    