import math
class Shape:
    def __init__(self, shape_type: str, size: float, name: str) -> None:
        self.__shape_type = shape_type.upper()
        self.size = size
        self.__name = name.upper()
        
    def __area(self) -> float:
        if self.__shape_type == "SQUARE":
            return self.size ** 2
        elif self.__shape_type == "CIRCLE":
            return (self.size**2)*math.pi
        elif self.__shape_type == "TRIANGLE":
            return (math.sqrt(3)/4)**(self.size**2)
        
    def get_info(self) -> str:
        return f"Shape: {self.__shape_type}, Size: {self.size:.2f}, Area: {self.area:.2f}, Name: {self.name}"
    
    def get_name(self) -> str:
        return self.__name
    
shape_list = []
while True:
    shape_type = input("Enter shape type: ").lower()
    if shape_type == "DONE":
        break
    try:
        size = float(input("Enter size: "))
        name = input("Enter name: ")
        if shape_type not in ["square", "circle", "triangle"]:
            raise ValueError("Invalid shape type")
        
        if size<0:
            raise ValueError("Invalid size")
        
        for i in shape_list:
            if i.get_name() == name:
                raise ValueError("Name already exists:")
            
    except ValueError as x:
        print(x)
        continue
    shape_list.append(Shape(shape_type,size,name))
    
print("-----REPORT-----")
if not shape_list:
    print(" No shapes recorded")
else:
    print(Shape.get_info())
            