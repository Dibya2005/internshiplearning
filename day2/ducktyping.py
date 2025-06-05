#DUck typing another way to achieve polymorphism besides inheritance object must have the minimum methods and attributes to be considered as a certain type
#if it lokks like a duck and quacks like a duck, it is a duck
class animal:
    alive=True
class dog(animal):
    def speak(self):
        return "Woof"
class cat(animal):
    def speak(self):
        return "Meow"
class car():
    alive=False
    def speak(self):
        return "Vroom"
animal=[dog(),cat(),car()] # car is not an animal but it has speak method
# this is an example of duck typing
for i in animal:
    # this will work, as both dog and cat are animals
    print(i.speak())
    print(i.alive) # this will work, as both dog and cat are animals
