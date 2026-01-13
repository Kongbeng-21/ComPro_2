class Shape:
    def __init__(self, shape_type, width, height):
        self.__shape_type = shape_type
        self.__width = width
        self.__height = height

    def print_info(self):
        area = 0.0
        if self.__shape_type.lower() == "triangle":
            area = 0.5 * self.__width * self.__height
        elif self.__shape_type.lower() == "rectangle":
            area = self.__width * self.__height
        else:
            print(f"Unknown shape: {self.__shape_type}")
            return

        print(f"Shape Type: {self.__shape_type} Width: {self.__width:.1f} Height: {self.__height:.1f} Area: {area:.1f}")


    def set_property(self, shape_type, width, height):
        self.__shape_type = shape_type
        self.__width = width
        self.__height = height