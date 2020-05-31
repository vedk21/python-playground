# Polymorphism (methods with same name but different functionalities)

class Car:
  def drive(self):
    print('driving a car')

class Mustang(Car):
  def __init__(self, color):
    self.color = color

  def drive(self):
    print('driving a car with boost')

class Camry(Car):
  def __init__(self, color):
    self.color = color

  def drive(self):
    print('driving a car with navigation enabled')

mustang = Mustang('grey')
camry = Camry('red')
car = Car('black')
mustang.drive() # 'driving a car with boost'
camry.drive() # 'driving a car with navigation enabled'
car.drive() # 'driving a car'

# here with every different type of object the same method behaves differently
