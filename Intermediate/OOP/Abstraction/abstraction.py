# Abstraction (hiding the details of operation but availabling the interface open)

class Car:
  def __init__(self, name, color, year):
    self.name = name
    self.color = color
    self._year = year # _ represents it understood as private member

  def drive(self):
    print('driving {self.name} a car of color {self.color}')

  def _get_year(self):
    return self._year

  def show_year(self):
    print(f'This car is manufactured in {self._get_year()}')

mustang = Car('Mustang GT', 'grey', 1970)
print(mustang.show_year())

# There is no way in python, that we can limit the member access using public or private key words,
# But it is a common practice to use '_' as representation of private members
