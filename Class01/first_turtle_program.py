from turtle import *

def main():
    leo = Turtle()
    leo.width(3)
    
    leo.up()
    leo.backward(200)
    leo.down()
    
    leo.forward(80)
    leo.left(60)
    leo.forward(110)
    
    leo.width(10)
    leo.right(150)
    leo.forward(100)
    leo.left(70)
    leo.backward(200)

    leo.pencolor("red")

    leo.forward(100)
    leo.left(120)
    
    leo.pencolor("blue")
    leo.forward(100)
    leo.left(120)
    
    leo.pencolor("purple")
    leo.forward(100)
    leo.left(120)

    print(leo.position())







# These two lines of code should appear at the bottom in all your programs
if __name__ == "__main__":
    main()