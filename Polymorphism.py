from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is Driving")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is Flying")

class Boat(Vehicle):
    def test(self):
        print(f"{self.name} is Testing")
    def move(self):
        print(f"{self.name} is Sailing")

def demonstrate_movement(vehicles):
    print("Demonstrating vehicle movements:")
    for vehicle in vehicles:
        vehicle.move()

# Creating instances of different vehicles
car = Car("Mercedes GLE")
plane = Plane("Boeing 747")
boat = Boat("Yacht")

# Demonstrating movement for all vehicles
vehicles = [car, plane, boat]
demonstrate_movement(vehicles)
