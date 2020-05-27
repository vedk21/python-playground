# __init__ constructor method

class Car:

  def __init__(self, name = 'no_name', year = 'very_old'):
    self.name = name
    self.year = year

no_name_car = Car()

print(no_name_car.name, no_name_car.year) # no_name very_old

# we can give default parameters to __init__ method
# first parameter has to be variable pointing to object itself (common practice is to use the name as self)