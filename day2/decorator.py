#decorator - a function that extends the behaviour of another function w/o modifying the base function
# pass the base funtion as an argument  to the decorator
# #def add_sprinkles(func):
#   
#     print("here is your sprinkle")
#     func()
#   if we dont have wrapper method the fonction will execute wilthout call but we dont want it

# def add_sprinkles(func):
#   def wrapper():
#     print("here is your sprinkle")
#     func()
#   return wrapper
# def addfudge(func):
#   def wrapper():
#     print("you add fudge")
#     func()
#   return wrapper
# @add_sprinkles
# @addfudge
# def getice(flavour):
#   print(f"here is your {flavour} icecream")
# getice("vanilla") #TypeError: add_sprinkles.<locals>.wrapper() takes 0 positional arguments but 1 was given

def add_sprinkles(func):
  def wrapper(*args,**kwargs):
    print("here is your sprinkle")
    func(*args,**kwargs)
  return wrapper
def addfudge(func):
  def wrapper(*args,**kwargs): #can take any number of arguments and keyword arguments
    print("you add fudge")
    func(*args,**kwargs)
  return wrapper
@add_sprinkles
@addfudge
def getice(flavour):
  print(f"here is your {flavour} icecream")
getice("vanilla") #TypeError: add_sprinkles.<locals>.wrapper() takes 0 positional arguments but 1 was given
