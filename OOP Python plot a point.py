import matplotlib.pyplot as plt

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    # add a self define add function to the point class
    def __add__(self, other):
        if isinstance (other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x,y)
        else:
            # if the + operation is not a Point(x,y) operation, then just do the addition
            x = self.x + other 
            y = self.y + other
            return Point(x,y)
    def plot(self):
        plt.scatter (self.x, self.y)

a = Point(0,2)
d = a+2

print(f"d.x: {d.x}, d.y: {d.y}")


