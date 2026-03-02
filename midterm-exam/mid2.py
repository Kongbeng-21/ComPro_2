class DisplayDevice:
    def __init__(self, name: str):
        self.__name = name
        
    def get_name(self) -> str:
        return self.__name
    
    def update(self, temp: float):
        print(f"{self.__name} received update: New temperature is {temp:.1f} C")
        
class WeatherStation:
    def __init__(self,temperature,observers):
        self.__temperature = 0.0
        self.temperature = temperature
        self.__observers = observers
        self.observers = []
        
    def register(self, device: DisplayDevice): 
        self.__observers.append(device)
        print(f"Registered: {device}")
        
    def unregister(self, device_name: str):
        for i in self.__observers:
            if i == device_name:
                self.__observers.remove(i)
                print(f"Unregistered: {device_name}")
            else:
                print("Device not found")
    @property
    def get_temperature(self) -> float:
        return self.__temperature
    

    def set_temperature(self, temp: float):
        self.temperature = temp
        for i in self.__observers:
            i.update(temp)
    
d = DisplayDevice
w = WeatherStation
observers = []
while True:
    cmd = input("Command: ")
    if cmd == ("DONE"):
        print(f"Final Temperature: {temp} C")
        break
    elif cmd == ("REGISTER"):
        device = input("Device Name: ")
        d1 = w(device)
        observers.append(device)
    elif cmd == ("UNREGISTER"):
        device = input("Device Name: ")
        WeatherStation.unregister()
    elif cmd == ("SET"):
        temp = float(input("Temperature: "))
    
        