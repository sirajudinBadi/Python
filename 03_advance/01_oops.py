from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 1/2*(self.base*self.height)
    
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return (self.width*self.length)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi*(self.radius**2)
    
shapes = [
    Triangle(10, 5),
    Rectangle(4, 6),
    Circle(7)
]

# for shape in shapes:
#     print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def start_engine(self):
        return "Bike starts.... Wooom wooom"

class Car(Vehicle):
    def start_engine(self):
        return "Car Starts.... Zoom zoom"
    
vehicles = [
    Bike(),
    Car()
]

# for vehicle in vehicles:
#     print(f"{vehicle.__class__.__name__} : {vehicle.start_engine()}")


class GrandFather():
    def __init__(self, grandfather_name, gf_wealth):
        self.grandfather_name = grandfather_name
        self.gf_wealth = gf_wealth
    
    def show(self):
        return f"1. I am {self.grandfather_name} having wealth of {self.gf_wealth} Rs."

class Father(GrandFather):
    def __init__(self,grandfather_name,gf_wealth, father_name, f_wealth):
        super().__init__(grandfather_name, gf_wealth)
        self.father_name = father_name
        self.f_wealth = f_wealth
    
    def show(self):
        return f"2. I am {self.father_name} {self.grandfather_name}. My father gave me wealth of {self.gf_wealth}. I have {self.f_wealth}."

class Child(Father):
    def __init__(self, grandfather_name, father_name, gf_wealth, f_wealth, child_name, c_wealth):
        super().__init__(grandfather_name, gf_wealth, father_name, f_wealth)
        self.child_name = child_name
        self.c_wealth = c_wealth
    
    def show(self):
        return f"3. I am {self.child_name} {self.father_name} {self.grandfather_name}. I have wealth of {self.c_wealth}. GF wealth = {self.gf_wealth}, F Wealth = {self.f_wealth}."

child1 = Child("Ratilal", "Rati", 9_00_000, 4_50_000, "Lal", 2_25_000)
print(child1.show())