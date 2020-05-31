# Super keyword

class Car:
  def __init__(self, year):
    self.year = year

  def drive(self):
    print('driving a car')

class Mustang(Car):
  def __init__(self, color, year):
    super().__init__(year)
    self.color = color

  def drive(self):
    print('driving a car with boost')

mustang = Mustang('grey', 1999)
print(mustang.year) # 1999
