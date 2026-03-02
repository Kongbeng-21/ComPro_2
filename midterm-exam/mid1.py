class Vehicle:
    def __init__(self, brand: str, cost: float, mileage: int):
        self._brand = brand
        self._cost = cost
        self.__mileage = mileage
    
    def get_mileage(self) -> int:
        return self.__mileage
    
    def __str__(self):
        return f"Vehicle: {self._brand} - ${self._cost:2f}"
    
class Car(Vehicle):
    def __init__(self, brand: str, cost: float, mileage: int, doors: int):
        super().__init__(brand, cost, mileage)
        self.__doors = doors
        
    def __str__(self):
        return f"Car: {self._brand} - ${self._cost} ({self.get_mileage()} km) / {self.__doors} Doors"
    
class Truck(Vehicle):
    def __init__(self, brand: str, cost: float, mileage: int, capacity: float):
        super().__init__(brand, cost, mileage)
        self.__capacity = capacity
        
    def __str__(self):
        return f"Truck: {self._brand} - ${self._cost} ({self.get_mileage()} km) / {self.__capacity}t Capacity"
    
    
fleet = []
while True:
    cmd = input("Command: ")
    if cmd == 'DONE':
        break
    
    elif cmd == "BUY":
        type = input("Type (Car/Truck): ")
        brand = input("Brand: ")
        cost = float(input("Cost: "))
        mileage = int(input("Mileage: "))
        if type == "car":
            doors = int(input("Doors: "))
            c1 = Car(brand,cost,mileage,doors)
            fleet.append(c1)
        elif type == "truck":
            capacity = float(input("Capacity: "))
            t1 = Truck(brand,cost,mileage,capacity)
            fleet.append(t1)

    elif cmd == "PURGE":
        mileage_limit = int(input("Mileage Limit: "))
        for i in fleet[::-1]:
            if mileage_limit > (i.get_mileage()):
                fleet.remove(i)
        print("Purged old vehicles")
            
print("-----Fleet Report-----")
if fleet == []:
    print("Fleet is empty")
else:
    for j in fleet:
        print(j)
