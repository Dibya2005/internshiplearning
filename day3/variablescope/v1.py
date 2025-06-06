#variable scope = where a variable is visible and can be accessed
# In Python, the scope of a variable is determined by where it is defined.
#scope resolution (LEGB)
#LEGB = Local, Enclosing, Global, Built-in
# def f1():
#   a= 1
#   print(a) #local scope
#   # print(b) #NameError: name 'b' is not defined
# def f2():
#   b= 2
#   print(b) #local scope
#   f1() #call f1() inside f2()
# #   # print(a) #NameError: name 'a' is not defined
# def f1():
#   a= 1
#   print(a) #local scope
# def f2():
#   a=2
#   print(a) #local scope
# f1() 
# f2() 
#first it will see local scope
#then it will see the enclosing scope
#then it will see the global scope
#then it will see the built-in scope
# def f3():
#   a=3
#   print(a) #local scope
#   def f4():
    
#     print(a) #a not in local scope so it will look in the enclosing scope
#   f4() #call f4() inside f3()
# f3()
#globel scope
# x=2
#  #local scope
# def f5():
#  print(x) #global scope
# f5()
from math import pi
def fun1():
  print(pi) #local scope
pi=2
fun1() #2
# because we look at globel scope first then the built-in scope