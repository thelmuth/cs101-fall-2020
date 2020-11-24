from PIL import Image

def main():
    
    image = Image.open("eliza.jpg")
#     image.show()
    
    my_pixel = Pixel((40, 100, 254))
    
    print(my_pixel.r)
    print(my_pixel.get_tuple())
    print("This should be False:", my_pixel.is_grayscale())
    
    gray_pixel = Pixel((92, 92, 92))
    print("This should be True:", gray_pixel.is_grayscale())
    
    print("Making my_pixel grayscale")
    my_pixel.make_grayscale()
    print(my_pixel.get_tuple())
    
#     detect_grayscale(image)
#     image.show()

    print(my_pixel)
    print(gray_pixel)
    
class Pixel():
    """Represents a pixel in an image."""
    
    def __init__(self, rgb):
        """This is the _Constructor_ for the class.
        This is called when we create a new Pixel object.
        Sets the object's initial state by setting attributes."""
        
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
        
    def get_tuple(self):
        """Returns tuple representation of this pixel."""
        return (self.r, self.g, self.b)
        
    def is_grayscale(self):
        """Return True if this pixel is grayscale, and False otherwise."""
        return self.r == self.g and self.g == self.b
    
    def set_rgb(self, r, g, b):
        """Sets the r, g, and b values of this pixel."""
        self.r = r
        self.g = g
        self.b = b
        
    def luminance(self):
        """Find and return the luminance of this pixel"""
        return (self.r + self.g + self.b) // 3
        
    def make_grayscale(self):
        """Changes a pixel's components to be grayscale."""
        
        lum = self.luminance()
        self.r = lum
        self.g = lum
        self.b = lum
        
    def __str__(self):
        """Must return a string representation of the object."""
        s = "(R: " + str(self.r) + ", G: " + str(self.g)
        s += ", B: " + str(self.b) + ")"
        return s

        
def detect_grayscale(image):
    """Detects grayscale pixels in an image, making them bright red.
    All other pixels are turned into grayscale to make it easier to see
    the red pixels."""
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = Pixel(image.getpixel((x, y)))
    
            if pixel.is_grayscale():
                ### Make this pixel bright red
                pixel.set_rgb(255, 0, 0)
            else:
                ### Make this pixel into grayscale
                pixel.make_grayscale()
            
            image.putpixel((x, y), pixel.get_tuple())
    
    
    
    
    
    
main()