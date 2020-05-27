# methods for class

class Car:
  total = 0

  def __init__(self, name = 'no_name', year = 'very_old', color = 'black'):
    self.name = name
    self.year = year
    self.color = color
    # increment total car count
    Car.total += 1

  @classmethod
  def get_special_car_model(cls, color):
    return cls('Special Sports Car', 2020, color)

  @staticmethod
  def get_stats():
    return f'The total number of cars sold are {Car.total}'

  # instance methods (takes self as mandatory parameter)
  def drive(self, max_speed):
    print(f'driving {self.name} car with {max_speed} km/hr max speed')

mustang = Car('Mustang GT', 1970)
db11 = Car('Aston Martin DB11', 1960)

mustang.drive(130) # driving Mustang GT car with 130 km/hr max speed
print(Car.get_stats()) # The total number of cars sold are 2
special_car = Car.get_special_car_model('golden')
print(special_car.color) # golden

