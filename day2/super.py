#super()=function used in a child class to call a method from the parent class
#allow you to call a method from the parent class without having to use the name of the parent class'
#Lesson 47: Super Function
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# super() = Function used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used.

#so with below, any similarities between square and cube,
# can move to rectangle. This will decrease repeat code.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def describe(self):
        return f"This is a rectangle"

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length * self.width
    def describe(self):
        parent_desc = super().describe()
        return f"{parent_desc} and also a square with length {self.length} and width {self.width}"

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length * self.width * self.height
    def describe(self):
        return f"This is a cube with length {self.length}, width {self.width} and height {self.height}"

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
print(square.describe())
print(cube.describe())
# print(square.volume()) # this will not work, as square does not have volume method
#super() is used to call the parent class's methods and attributes it can be used in child class constructor to assign values to the parent class's attributes