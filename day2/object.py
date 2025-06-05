#object = a bundle of data and methods
#ex ample: a car is an object
# car has attributes like color, model, and methods like start, stop
class Car:
    def __init__(self, color, model): # constructor dunder init method
        self.color = color
        self.model = model
        self.speed = 0
    def drive(self, speed):
        self.speed = speed
        print(f"The {self.color} {self.model} is driving at {self.speed} km/h.")
    def stop(self):
        self.speed = 0
        print(f"The {self.color} {self.model} has stopped.")
    def define(self):
        print(f"This is a {self.color} {self.model} car.")
car1 = Car("red", "Toyota")
car2 = Car("blue", "Honda")
car1.drive(60)
car2.drive(80)
car1.stop()
car2.stop()
car1.define()
car2.define() 
print(car1.color) # red
print(car1.model) # Toyota
print(car1.speed) # 0
print(car2.color) # blue
print(car2.model) # Honda