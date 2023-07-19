# OOP Python
# Class and Object
import turtle #a library for drawing

class Polygon:
    def __init__(self, sides, name, size = 100, color = "red", line_thickness = 2):
        self.sides = sides
        self.name = name
        self.interior_angles = (self.sides - 2) * 180
        self.angle = self.interior_angles / self.sides  
        self.size = size
        self.color = color
        self.line_thickness = line_thickness

    def draw (self): # self make us refer to the init self.variables
        turtle.color(self.color)
        turtle.pensize (self.line_thickness)
        for i in range (self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        # turtle.done()

# create a sub class
class Square (Polygon):
    # we can re define the init function
    def __init__(self, size = 100, color = "black", line_thickness = 2):
        #
        super().__init__(4, "Square", size, color, line_thickness)

    # override the draw function
    def draw (self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()
        turtle.done()

s = Square(color = "blue", line_thickness = 5)
print(s.sides, s.name)
print(s.draw())

#creating objects
# square = Polygon( 4 , "Square") # set sides and name for Polygon, encapsulate information through this Polygon class
# print(f"Name : {square.name} \nSides: {square.sides} \nInbterior_angles: {square.interior_angles} \nEach_Angle: {square.angle}")
# square.draw()
# hex = Polygon( 6 , "hexagon") # set sides and name for Polygon, encapsulate information through this Polygon class

# hex.draw()