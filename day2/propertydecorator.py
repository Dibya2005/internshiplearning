#@property = decorator used to deffine a meythod as a property it can be accesed like an attribute
# benefit - add addtional logic when read write or delete an attribute
#gives you getter setter and deleter method
class rectagle:
  def __init__(self, width, height):
    self._width=width #make your instace method make it protected
    self._height=height
  @property
  def width(self):
    return f"{self._width:.1f} cm"
  @property
  def height(self):
    return f"{self._height:.1f} cm"
  @width.setter
  def width(self,new_width):
    if new_width>0:
      self._width=new_width
    else:
      print("width must be greater than zero")
  @width.setter
  def width(self,new_width):
    if new_width>0:
      self._width=new_width
    else:
      print("width must be greater than zero")
  @width.deleter
  def width(self):
    del self._width
    print("width has been deleted")
  @height.deleter
  def height(self):
    del self._height
    print("width has been deleted")

rect=rectagle(3,6)
rect.width=7
del rect.width
# print(rect.width)
print(rect.height)
#accesing the witdh or height will be return whatever is in the method