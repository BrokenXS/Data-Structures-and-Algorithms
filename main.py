from car import AutonomousElectricCar, Car, ElectricCar
car1 = Car("BB", 2024, "red", False)
car2 = Car("AA", 2024, "red", False)
car = Car("Toyota Corolla", 2020, "red", True)

electric_car = ElectricCar("Tesla Model 3", 2023, "blue", False, "Toan", 25, 75)

# Create an instance of AutonomousElectricCar
autonomous_car = AutonomousElectricCar("Tesla Model X", 2023, "black", True,"Minh", 27, 100, 5)

# Access the class variable
print(f"Total cars created: {Car.total_cars}")

print(electric_car.drive())  # Output: The blue Tesla Model 3 is now driving.
print(electric_car.charge())  # Output: The blue Tesla Model 3 is charging with a 75 kWh battery.
print(electric_car.getUser()) 

# Access methods from all levels of the hierarchy
print(autonomous_car.getUser())
print(autonomous_car.drive())  # Output: The black Tesla Model X is now driving.
print(autonomous_car.charge())  # Output: The black Tesla Model X is charging with a 100 kWh battery.
print(autonomous_car.self_drive())  # Output: The black Tesla Model X is driving autonomously at level 5.
