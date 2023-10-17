def double(s):
    if isinstance(s, Circle):
        s.radius *= 2
    elif isinstance(s,Rectangle):
        s.width *= 2
        s.height *= 2
    
def create_double(s):
    if isinstance(s, Circle):
        return Circle(s.radius * 2)
    elif isinstance(s, Rectangle):
        return Rectangle(s.width *2, s.height * 2)

# Do not change the code below this line.
#########################################
class Circle:
    def __init__(self, r=1):
        self.radius = r
    def __str__(self):
        return "Circle of radius " + str(self.radius)

class Rectangle:
    def __init__(self, w=1, h=1):
        self.width = w
        self.height = h
    def __str__(self):
        return "Rectangle of width " + str(self.width) + " and height " + str(self.height)

r  = int(input())
w = int(input())
h = int(input())

cir1 = Circle(r)
rec1 = Rectangle(w,h)
print(cir1)
print(rec1)

double(cir1)
double(rec1)
print(cir1)
print(rec1)

cir2 = create_double(cir1)
rec2 = create_double(rec1)
print(cir2)
print(rec2)

print(cir1)
print(rec1)