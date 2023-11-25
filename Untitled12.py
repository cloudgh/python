from abc import ABC, abstractmethod

class Technology(ABC):
    def __init__(self, brand, model, year, weight):
        self.brand = brand
        self.model = model
        self.year = year
        self.weight = weight

    @abstractmethod
    def start(self):
        pass

class Car(Technology):
    def __init__(self, brand, model, year, weight, fuel_type):
        super().__init__(brand, model, year, weight)
        self.fuel_type = fuel_type

    def start(self):
        return f"The {self.year} {self.brand} {self.model} car is running."

class Computer(Technology):
    def __init__(self, brand, model, year, weight, operating_system):
        super().__init__(brand, model, year, weight)
        self.operating_system = operating_system

    def start(self):
        return f"The {self.year} {self.brand} {self.model} computer is booting up."



car = Car("Toyota", "Camry", 2022, 1500, "Gasoline")
computer = Computer("Apple", "MacBook Pro", 2021, 2.0, "macOS")

print(car.start())      
print(computer.start()) 

# brand и model  предоставляют базовую информацию о технике, которая может быть общей любых устройств.

# year  полезен для техники, так как год выпуска может влиять на ее характеристики, производительность и технологии.

# weight Вес также является общей характеристикой для различных видов техники и может быть важным для понимания их  использования.