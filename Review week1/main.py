from shape import Shape

def main():
    shape = []
    x = ''  # Initialize x to enter the loop
    while x != '5':
        print('Menu')
        print('1. Add a shape')
        print('2. Update a shape')
        print('3. Delete a shape')
        print('4. Display all shapes')
        print('5. Exit')
        x = input('Enter your choice: ')
        if x == '1':
            st = input('Enter the shape type (t for Triangle/r for Rectangle): ').lower()
            shape_type = "Triangle" if st == "t" else "Rectangle"
            width = float(input("Enter the width of the shape: "))
            height = float(input("Enter the height of the shape: "))
            shp = Shape(shape_type,width,height)
            shape.append(shp)
            print("Shape added successfully!")
        elif x == '2':
            index = int(input("Enter the index of the shape to update: "))
            st = input("Enter the new shape type (t for Triangle/r for Rectangle): ")
            shape_type = "Triangle" if st == 't' else "Rectangle"
            width = float(input("Enter the new width of the shape: "))
            height = float(input("Enter the new height of the shape: "))
            shape[index].set_property( shape_type, width, height)
            print("Shape updated successfully!")
        elif x == '3':
            index = int(input("Enter the index of the shape to delete: "))
            shape.pop(index)
            print("Shape deleted successfully!")
        elif x == '4':
            for i,shp in enumerate(shape):
                print(f"Shape {i} --> ",end="")
                shp.print_info()
                
        elif x == '5':
            print('Exiting...')
            break
        else:
            print('Invalid choice! Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()