#inheritance = allows a class to inherit attributes and methods from another class
#help with code reuse and organization
#example: a car is a vehicle, so we can create a Vehicle class and inherit from it
# class child_class(parent_class):
class animal:
    def __init__(self, name):
        self.name = name
        self.isalive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")



class dog(animal):
    pass
    def speak(self):
        print(f"{self.name} barks")
class cat(animal):
    pass
dog = dog("lassie")
cat = cat("whiskers")
print(dog.name)
print(cat.name)
dog.eat()
cat.eat()
dog.sleep()
cat.sleep()
dog.speak()
cat.speak()