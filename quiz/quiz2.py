class Product:
    def __init__(self, name: str, price: float, stock: int):
        self._name = name
        self._price = price
        self.__stock = stock
        
    def get_stock(self) -> int:
        return self.__stock
    
    def __str__(self):
        return f"Product: {self._name} - ${self._price} (Qty: {self.__stock})"
    
class Electronics(Product):
    def __init__(self, name: str, price: float, stock: int, warranty: int):
        super().__init__(name, price, stock)
        self.__warranty = warranty
        
    def __str__(self):
        return f"Electronics: {self._name} - ${self._price} (Qty: {self.get_stock()}) / {self.__warranty}mo Warranty"
    
    
    
class Clothing(Product):
    def __init__(self, name: str, price: float, stock: int, material: str):
        super().__init__(name, price, stock)
        self.__material = material
    
    def __str__(self): 
        return f"Clothing: {self._name} - ${self._price} (Qty: {self.get_stock()}) / {self.__material}"
    
inventory = []
while True:
    cmd = input("Command: ").upper()
    if cmd == "DONE":
        break
    elif cmd == ("ADD"):
        type = input("Type (Elec/Cloth): ").lower()
        name = input("Name: ")
        price = input("Price: ")
        stock = input("Stock: ")
        
        if type == ("elec"):
            warranty = input("Warranty: ")
            inventory.append(Electronics(name,price,stock,warranty))
            
        elif type == ("cloth"):
            material = input("Material: ")
            inventory.append(Clothing(name,price,stock,material))
    elif cmd == ("CLEAR"):
        threshold= int(input("Stock Threshold: "))
        inventory.remove(Product(threshold,0))
        print("Removed low stock items")

print("-----Inventory Report-----")
if not inventory:
    print("Store is empty")
else:
    for i in inventory:
        print(i)
          