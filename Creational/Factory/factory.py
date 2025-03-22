from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass  # Abstract method (subclasses must implement this)

# Concrete classes
class Circle(Shape):
   
    def draw(self):
        print("Circle is drawing")

class Square(Shape):
   

    def draw(self):
        print("Square is drawing")

# Factory class
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        shape_class = eval(shape_type)  # Convert string to class reference
        return shape_class()  # Create an instance

# Usage
shape = ShapeFactory.get_shape("Circle")  # Returns an instance of Circle
shape.draw()  # ✅ Output: Circle instance created -> Circle is drawing

shape2 = ShapeFactory.get_shape("Square")
shape2.draw()  # ✅ Output: Square instance created -> Square is drawing
