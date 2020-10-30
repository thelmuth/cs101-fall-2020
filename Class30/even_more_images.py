import os
from PIL import Image

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():

    directory = os.getcwd()
    
    ### Opens the image from the current working directory
    kids = Image.open(directory + "/box.jpg")
#     kids.show()

    ### Detect the edges
#     new_kids = edge_detect(kids, 30)
#     new_kids.show()

    ### Write a function that generates an image from scratch
#     gradient = make_gradient()
#     gradient.show()

    ### Rotate image
#     rotated = rotate(kids)
#     rotated.show()

    ### Resize the image
#     smaller = resize(kids, 200)
#     smaller.show()
    
#     smaller = resize(kids, 20)
#     smaller.show()

    larger = resize(kids, 1500)
    larger.show()
    
def resize(image, new_width):
    """Resizes the image to have the new_width as its width, and a corresponding
    new height of the same proportion."""
    
    ### Calculate new height
    new_height = new_width * image.height // image.width
    new_image = Image.new("RGB", (new_width, new_height))
    
    ### We'll multiply every x and y value with this to find the pixel
    ### to read in the old image
    pixel_change_factor = image.width / new_width
    
    for x in range(new_width):
        print("we're at x value of", x)
        
        for y in range(new_height):
            
            old_x = int(x * pixel_change_factor)
            old_y = int(y * pixel_change_factor)
            
            pixel = image.getpixel((old_x, old_y))
            new_image.putpixel((x, y), pixel)
            
    return new_image
    
    
def rotate(image):
    """Rotates and image 90 degrees"""
    
    new_image = Image.new("RGB", (image.height, image.width))
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            
            ### Calculate that pixel's location in new_image
            new_x = image.height - y - 1
            new_y = x

            
            new_image.putpixel((new_x, new_y), pixel)
            
    return new_image


def make_gradient():
    """Make a new image with a gradient of color."""
    
    image = Image.new("RGB", (256, 256))
    
    for x in range(image.width):
        for y in range(image.height):
            
            ### Make an orange square
#             image.putpixel((x, y), (255, 180, 0))

            # Use x or y in the color
            image.putpixel((x, y), (x, x, x))

            ### Green to purple gradient
#             image.putpixel((x, y), (x, 128, x))
            
            ### Red to cyan gradient from lower-left to upper-right
#             image.putpixel((x, y), (y, x, x))

            ### Weird color mixing!
#             image.putpixel((x, y), (y, 128, x))
            
            
    return image


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
    
    new_image = Image.new("RGB", (image.width - 1, image.height - 1))
    
    new_image.show()
    
    for x in range(new_image.width):
        print(x)
        
        for y in range(new_image.height):
            
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
                new_image.putpixel((x, y), BLACK)
            elif abs(lum_pixel - lum_down) > luminance_threshold:
                new_image.putpixel((x, y), BLACK)
            else:
                new_image.putpixel((x, y), WHITE)
    
    return new_image
    


if __name__ == "__main__":
    main()
    