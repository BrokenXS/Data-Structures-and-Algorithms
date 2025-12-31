# @property = Decorator that allows you to define methods in a class that can be accessed like attributes.

class Reactangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return f"{self._width} units"
    
    @property
    def height(self):
        return f"{self._height} units"
    
    @property
    def area(self):
        return self._width * self._height

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
        
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
        
    @width.deleter
    def width(self):
        del self._width
rect = Reactangle(2, 10)

print(rect.width)
print(rect.area)