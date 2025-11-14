class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"


#Car have no relation to Animal
#Car have param and function with the same name as Animal subclasses
#Consider it polymorphism
class Car:
    alive = False
    def speak(self):
        return "Vroom!"

animals = [Dog(), Cat(), Car()]

for animal in animals:
    print(animal.speak())
    print(animal.alive)