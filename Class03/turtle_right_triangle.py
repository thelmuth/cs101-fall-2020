from turtle import *
import math

def main():

    april = Turtle()
    april.width(3)

    pedro = 37

    # Variable is on the left, and the expression is on the right
    side1 = int(input("Enter the length of a side of a triangle: "))
    side2 = side1
    
    # We can use variables in other expressions
    
    hypotenuse = math.sqrt((side1 * side1) + (side2 * side2))
    
    print("The hypotenuse is", hypotenuse, ". There you have it!")
    
    # Draw a triangle
    
    april.fillcolor("darkorchid")
    april.begin_fill()
    
    april.forward(side1)
    april.left(90)
    april.forward(side2)
    april.left(135)
    april.forward(hypotenuse)
    april.left(135)
    
    april.end_fill()
    
    # Draw a second triangle
    
    # First, move the turtle somewhere else
    april.up()
    april.goto(-200, 100) # This tells the turtle to go to a specific location
    april.down()
    april.left(72)
    
    # Now, draw a 30-60-90 triangle
    
    side1 = 78
    hypotenuse = side1 * 2
    
    # Calculate the length of side2
    side2 = math.sqrt(hypotenuse * hypotenuse - side1 * side1)
    
    april.fillcolor("limegreen")
    april.begin_fill()
    
    april.pencolor("red")
    
    april.forward(side1)
    april.left(180 - 60)
    april.forward(hypotenuse)
    april.left(180 - 30)
    april.forward(side2)
    april.left(90)
    
    april.end_fill()



# These two lines of code should appear at the bottom in all your programs
if __name__ == "__main__":
    main()
