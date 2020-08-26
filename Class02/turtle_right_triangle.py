from turtle import *
import math

def main():

    april = Turtle()
    april.width(3)

    side1 = 129 # Variable is on the left, and the expression is on the right
    side2 = 129
    
    # We can use variables in other expressions
    
    hypotenuse = math.sqrt((side1 * side1) + (side2 * side2))
    
    print(hypotenuse)
    
    # Draw a triangle
    
    april.forward(side1)
    april.left(90)
    april.forward(side2)
    april.left(135)
    april.forward(hypotenuse)
    april.left(135)



# These two lines of code should appear at the bottom in all your programs
if __name__ == "__main__":
    main()
