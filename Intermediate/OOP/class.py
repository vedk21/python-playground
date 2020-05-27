# Class in python (Blueprint for objects)

class Car:
  def __init__(self, name, year):
    self.name = name
    self.year = year

mustang = Car('Mustang GT', 1970) # object instantiation
db11 = Car('Aston Martin DB11', 1960) # object instantiation

print(mustang.name) # Mustang GT
print(db11.name, db11.year) # Ashton Martin DB11 1960
