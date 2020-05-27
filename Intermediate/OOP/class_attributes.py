# Class attributes

class Car:
  # class attributes
  total = 0

  def __init__(self, name, color, year):
    # object attributes
    self.name = name
    self.color = color
    self.year = year
    # increment car total
    Car.total += 1

# instantiate cars
mustang = Car('Mustang GT', 'red', 1970)
db11 = Car('Aston Martin DB11', 'grey', 1960)

print(db11.year) # 1960
print(mustang.color) # red
print(Car.total) # 2
print(mustang.total) # 2 (we can also access class attributes using objects)
