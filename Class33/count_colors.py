import os
from PIL import Image

def main():
    directory = os.getcwd()

    kids = Image.open(directory + "/box.jpg")
    
#     kids.show()
    
    ### How many colors are possible?
    print("There are 256^3 =", 256 ** 3)
    
    ### How many pixels are in this image?
    print("There are", kids.width * kids.height, "pixels in this image.")
    
    ### How many unique colors are in this image?
#     colors = []

    colors = {}
    
    for x in range(kids.width):
        print("x value", x)
        for y in range(kids.height):
            pixel = kids.getpixel((x, y))
            
            if pixel not in colors:
#                 colors.append(pixel)
                colors[pixel] = 1
                
    print("The number of distinct colors in image is", len(colors))
    
    

if __name__ == "__main__":
    main()
    