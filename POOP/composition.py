# Compositon is own-aship based relationship where one class contains
# an object of another class as a part of its state.


class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
class Wheel:
    def __init__(self, size):
        self.size = size
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)  # Car "owns" the Engine
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]  # Car "owns" 4 Wheels
    
    def display_info(self):
        print(f"Car: {self.make} {self.model}")
        print(f"Engine Horse Power: {self.engine.horse_power}")
        print(f"Wheel Size: {self.wheels[0].size} inches")
        
car = Car(make="Toyota", model="Camry", horse_power=200, wheel_size=16)
car.display_info()
            