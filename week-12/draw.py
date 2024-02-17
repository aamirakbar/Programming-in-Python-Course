import turtle

from shapes import *

def draw_shape(shape):
    window = turtle.Screen()
    window.title("Shapes")

    pen = turtle.Turtle()
    pen.speed(2)
    
    area = None  # Placeholder for the area value

    if isinstance(shape, Rectangle):
        pen.forward(shape.length)
        pen.left(90)
        pen.forward(shape.breadth)
        pen.left(90)
        pen.forward(shape.length)
        pen.left(90)
        pen.forward(shape.breadth)
        area = shape.area()

    elif isinstance(shape, Circle):
        pen.circle(shape.radius)
        area = shape.area()

    elif isinstance(shape, Square):
        for _ in range(4):
            pen.forward(shape.side)
            pen.left(90)
        area = shape.area()

    elif isinstance(shape, Triangle):
        pen.forward(shape.base)
        pen.left(135)
        pen.forward(shape.height)
        pen.left(90)
        pen.forward(shape.height)
        pen.left(135)
        area = shape.area()
        
    # Display area on the GUI window
    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    pen.write(f"Area: {area}", align="center", font=("Arial", 16, "normal"))

    window.mainloop()

# Example usage
rectangle = Rectangle(100, 90)
circle = Circle(80)
square = Square(80)
triangle = Triangle(40, 30)

#draw_shape(rectangle)
#draw_shape(circle)
#draw_shape(square)
draw_shape(triangle)
