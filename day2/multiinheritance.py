#Lesson 44: Multiple  Inheritance
# https://www.youtube.com/watch?v=XKHEtdqhLK8
#Multiple Inheritance = when a child class is derived from more than one parent class

#this is used when want to create a class that needs different attributes/methods from multiple classes.
#so below some animals are both prey and predator (e.g. fish)
class Animal:
    def __init__(self, name): #if you not assigmnming any attiribute or you dont need to use __init__ method, you can just use pass
        #this is the constructor method, it is called when an object is created
        self.name = name
        self.isalive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Prey(Animal):
    def flee(self):
        print("This animal flees")
class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Hawky")
fish = Fish('Nemo')
rabbit.eat()

#as can be seen below, only fish has flee and hunt.
#rabbit.flee()
#hawk.hunt()
#fish.hunt()
#fish.flee()