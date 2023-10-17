class Circle:
    def __init__(self, w = 2, h = 1):
        self.width = w
        self.height = h
        
    def getArea(self):
        return self.width*self.height
            
    def getPerimeter(self):
        return (self.width+self.height)*2
            
recA = Circle()
recB = Circle(int(input()), int(input()))
print(recA.getArea())
print(recA.getPerimeter())
print(recB.getArea())
print(recB.getPerimeter())