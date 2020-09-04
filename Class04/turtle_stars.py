from turtle import *

def main():

    larry = Turtle()
    
    # These things happen before the loop starts
    larry.width(5)
    larry.pencolor("crimson")
    larry.up()
    larry.forward(100)
    larry.down()
    
#     larry.setheading(270)
    
    for _ in range(8):
        # Code here will run every time through the loop.
        larry.forward(100)
        larry.right(90 + 45)
    
    # Code that should run after the loop has finished
    # looping should be unindented.
    # This code will only run once.
    
    larry.color("gray")
    larry.up()
    larry.backward(200)
    larry.down()
    
    for _ in range(5):
        ### This would make a square at the end of every point of the star.
#         for _ in range(4):
#             larry.forward(25)
#             larry.right(90)
        
        larry.forward(100)
        larry.right(90 + 54)
    
    
    
    
    



# These two lines of code should appear at the bottom in all your programs
if __name__ == "__main__":
    main()
