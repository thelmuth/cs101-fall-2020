from turtle import *


def greet(greeting, name="person", question="How are you?"):
    print(greeting, name + ".", question)

# greet("Howdy")
# 
# greet("Hi", "Andrew")
# 
# greet("Zoinks", question = "What is your status?")
# 
# greet(question = "What?", greeting = "hello")

def area_of_rectangle(length, width = None):
    """Returns the area of a rectangle. If width isn't given,
    treats rectangle as a square"""
    
    if width == None:
        width = length
    
    return length * width

# print(area_of_rectangle(5, 4))
#     
# print(area_of_rectangle(7))

def draw_triangle(turt, side_length=100, color="white", pen_width=3):
    """Draws a triangle with a turtle"""
    
    turt.fillcolor(color)
    turt.width(pen_width)
    
    turt.begin_fill()
    for _ in range(3):
        turt.forward(side_length)
        turt.left(120)
    
    turt.end_fill()
    
    return side_length
    
frank = Turtle()
val = draw_triangle(frank)

print(val)

frank.right(90)
frank.forward(100)

draw_triangle(frank, color = "green", pen_width = 10)
    
    
    
