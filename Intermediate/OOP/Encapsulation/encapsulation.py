# Encapsulation (packing the attributes and methods of a class together)
# attributes are properties of objects and methods are actions

class Car:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def drive(self):
    print('driving {self.name} a car of color {self.color}')

mustang = Car('Mustang GT', 1970)
