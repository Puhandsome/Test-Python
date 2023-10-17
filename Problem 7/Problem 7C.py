pi = 3.14159

class Circle:
# Provide the code for the class Circle here

    def __init__(self, radius:float = 10.0, x:float = 0.0, y:float = 0.0):
        self.radius = float(radius)
        self.x = float(x)
        self.y = float(y)
        
    def getArea(self):
        return pi*(self.radius**2)
    
    def getPerimeter(self):
        return pi*(self.radius*2)
    
    def moveTo(self,new_x = int, new_y = int):
        self.x = new_x
        self.y = new_y
    def is_inside(self, c: "Circle"):
        dx = c.x - self.x
        dy = c.y - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist == 0:
            return self.radius <= c.radius
        
        dx2 = self.radius * dx / dist
        dy2 = self.radius * dy / dist
        dist2 = (dx2**2 + dy2**2)**0.5
        return dist + dist2 <= c.radius
    
    def getEnclosingCircle(self,c):
        if self.is_inside(c):
            return Circle(c.radius, c.x, c.y)
        elif c.is_inside(self):
            return Circle(self.radius, self.x, self.y)
        
        dx = c.x - self.x
        dy = c.y - self.y
        dist = (dx**2 + dy**2)**0.5
        
        x1 = self.x - dx * self.radius / dist
        y1 = self.y - dy * self.radius / dist
        x2 = c.x + dx * c.radius / dist
        y2 = c.y + dy * c.radius / dist
        
        diameter = ((x2 - x1)**2 + (y2-y1)**2)**0.5
        radius = diameter/2
        x = (x1+x2) /2
        y = (y1+y2) /2
        return Circle(radius,x,y)
    
    
# Do NOT change the code below
cirA = Circle()
cirB = Circle(int(input()))
cirB.moveTo(int(input()),int(input()))
print(round(cirB.getArea(),2))
print(round(cirB.getPerimeter(),2))
cirC = cirA.getEnclosingCircle(cirB)
print(round(cirC.radius,2))
print(round(cirC.x,2))
print(round(cirC.y,2))