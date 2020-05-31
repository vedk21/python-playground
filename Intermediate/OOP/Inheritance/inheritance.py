# Inheritance (parent - child classes)

class Car:
  def drive(self):
    print('driving a car')

class Mustang(Car):
  def __init__(self, color):
    self.color = color

  def boost(self):
    print('driving a car with boost')

class Camry(Car):
  def __init__(self, color):
    self.color = color

  def navigation(self):
    print('driving a car with navigation enabled')

mustang = Mustang('grey')
camry = Camry('red')
mustang.boost() # 'driving a car with boost'
camry.navigation() # 'driving a car with navigation enabled'
mustang.drive() # 'driving a car'
camry.drive() # 'driving a car'

# isinstance
print(isinstance(camry, Camry)) # True
print(isinstance(camry, Car)) # True
print(isinstance(camry, Mustang)) # False
print(isinstance(camry, object)) # True
