#static method =method that belongs to the class and not to the instance of the class
# #it can be called without creating an instance of the class
# #it does not require self parameter
#it used in general utility functions that do not require access to the instance or class
#instance method =method that belongs to the instance of the class(object)
#static method =best for utility functions that do not require access to the instance or class
#instance method
#def instance_method(self):
#     return f"{self.name} is an instance method"
#@staticmethod
#def static_method(kilometers):
#     return kilometers * 0.6213
class employee:
    #class variable
    company="Google"
    #constructor
    def __init__(self, name, age,position):
        self.position=position
        self.name=name
        self.age=age
    #instance method
    def info(self):
        return f"{self.name} is {self.age} years old"
    #static method
    @staticmethod
    def is_validpos(position):
          validpos= ["Manager", "Developer", "Designer"]
          return position in validpos
    #we dont need to create an instance of the class to call the static method
print(employee.is_validpos("Manager")) # this will return True
emp1=employee("John", 25,"Developer")
emp2=employee("Jane", 30,"Designer")
print(emp1.info()) # this will return John is 25 years old
