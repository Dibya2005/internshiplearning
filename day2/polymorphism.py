#polymorphism= greek word meaning "many shapes"
#two ways to achieve polymorphism in python
#1. inhetritance=obnject to treated as same type as its parent class
#2. duck typing=objects are interchangeable if they have the same methods and attributes
from abc import ABC, abstractmethod
#abstract class=class that cannot be instantiated and must be subclassed
class shape:
  pass
  @abstractmethod #abstract method=method that has no implementation and must be implemented in the subclass
  #abstract method is a method that is declared but contains no implementation

  def area(self):
    pass
class square(shape):
  def __init__(self, length):
    self.length = length
  def area(self):
    return self.length * self.length
    
    
  
class circle(shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return 3.14 * self.radius * self.radius
  
class triangle(shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height
  def area(self):
    return 0.5 * self.base * self.height
class pizza(circle):
  def __init__(self, radius):
    super().__init__(radius) # call the parent class constructor
    
    self.topping = "cheese"
 # squre is a shape not a triangle or circle
shape=[circle(4),square(5),triangle(6,7),pizza(8)] #pizza is now both a circle and a shape
# shape is a list of objects of different classes
#this is an example of polymorphism
for i in shape:
  print(i.area()) #pizza is not a shape but it has area method
# print(i.topping) # this will not work, as i is a shape object and does not have topping attribute
