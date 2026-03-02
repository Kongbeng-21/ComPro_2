import math
class Shape:
    def __init__(self,name:str):
        self.__name = name
        
    def name(self):
        return self.__name.upper()
    
    def area(self) -> float:
        return 0.0
    
    def __str__(self):
        return f"Shape: {self.name()}, Area: {self.area():.2f}"
    
    def __lt__(self, other):
        if self.area() < other.area():
            return True
        
class Square(Shape):
    def __init__(self, name: str, side: float):
        super().__init__(name)
        self.__side = side
        
    def side(self):
        if self.__side <= 0:
            print("Invalid side")
        else:    
            return self.__side
    
    def area(self):
        return self.__side**2
    
    def __str__(self):
        return f"Square {self.name()}: Side {self.side():.2f}, Area {self.area():.2f}"
    
class Circle(Shape):
    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self.__radius = radius
        
    def radius(self):
        if self.__radius <= 0:
            print("Invalid radius")
        else:
            return self.__radius
        
    def area(self):
        return math.pi * self.radius()**2
    
    def __str__(self):
        return f"Circle {self.name()}: Radius {self.radius():.2f}, Area {self.area():.2f}"
    
    
shapes = []
while True:
    type = input("Enter type (Square/Circle): ")
    if type == ("DONE"):
        break
    elif type not in ["Square","Circle"]:
        print("Invalid type")
        continue
    name = input("Enter name: ")  
    
    if type == ("Square"):
        try:
            side = float(input("Enter size: "))
            shapes.append(Square(name,side))
            if str(side) is True:
                raise ValueError("Invalid input")    
                
            elif side <=0:
                raise ValueError("Invalid size")
        except ValueError as x:
            print(x)
            continue       
        
    elif type == ("Circle"):
        radius = float(input("Enter size: ")) 
        shapes.append(Circle(name,radius))
        
        if radius <=0:
            print("Invalid size")
        
    
    

    
print("-----Unsorted-----")
for i in shapes:
    print(i.__str__())
print("-----Sorted (by Area)-----")
for i in shapes:
    print(i.__lt__())
