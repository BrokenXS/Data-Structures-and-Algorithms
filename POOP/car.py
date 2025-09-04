class Car:
    
    total_cars = 0
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        # Increment the class variable whenever a new car is created
        Car.total_cars += 1
        
    def drive(self):
        return f"The {self.color} {self.model} is now driving."

    def stop(self):
        return f"The {self.color} {self.model} has stopped."

# New parent class for multiple inheritance
# Mutilevel inheritance
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getUser(self):
        return f"The User with name {self.name} is the owner"
    
# Subclass inheriting from both Car and Battery
class ElectricCar(Car, User):
    def __init__(self, model, year, color, for_sale, name, age, battery_capacity):
        self.battery_capacity = battery_capacity
        # Initialize Car attributes
        Car.__init__(self, model, year, color, for_sale)
        # Initialize User attributes
        User.__init__(self, name , age)

    def charge(self):
        return f"The {self.color} {self.model} is charging with a {self.battery_capacity} kWh battery."

# Final class inheriting from ElectricCar
class AutonomousElectricCar(ElectricCar):
    def __init__(self, model, year, color, for_sale, name, age, battery_capacity, autonomous_level):
        # Initialize ElectricCar attributes
        super().__init__(model, year, color, for_sale, name, age, battery_capacity)
        self.autonomous_level = autonomous_level

    def self_drive(self):
        return f"The {self.color} {self.model} is driving autonomously at level {self.autonomous_level}."