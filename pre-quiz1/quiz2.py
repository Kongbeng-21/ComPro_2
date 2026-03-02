import math
class Shape:
    def __init__(self, shape_type: str, size: float, name: str) -> None:
        self.__shape_type = shape_type.upper()
        self.__size = size
        self.__name = name.upper()
        
    def __area(self) -> float:
        if self.__shape_type == "square":
            return self.__size**2
        elif self.__shape_type == "circle":
            return (self.__size**2) * math.pi
        elif self.__shape_type == "triangle":
            return (self.__size**2)*(math.sqrt(3))/4

    
    def get_info(self) -> str:
        return f"Shape: {self.__shape_type}, Size: {self.__size:.2f}, Area: {self.__area():.2f}, Name: {self.__name}"
    
    def get_name(self) -> str:
        return self.__name
    
shape_list = []
while True:
    shape_type = input("Enter shape type: ").lower()
    if shape_type == "done":
        break
    if shape_type not in ["square","circle","triangle"]:
        print("Invalid shape type")
        continue
    try:
        size = float(input("Enter size: "))
        if size < 0:
            print("Invalid size")
            continue
    except ValueError:
        print("Invalid size")
    name = input("Enter name: ").upper()
    names = []
    for i in shape_list:
        names.append(i.get_name())
    if name in names:
        print(f"Name already exists: {name}")
        continue
    
    s = Shape(shape_type,size,name)    
    shape_list.append(s)

print("-----REPORT-----")
if not shape_list:
    print("No shapes recorded") 
else:
    for i in shape_list:
        print(i.get_info())
    