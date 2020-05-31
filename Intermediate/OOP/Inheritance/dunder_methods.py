# Dunder methods (special methods which start and end with __)

class Car:
  def __init__(self, year, parts):
    self.year = year
    self.parts = parts

  def drive(self):
    print('driving a car')
  
  def __len__(self): # overriding the dunder methods
    return len(self.parts)

  def __getitem__(self, index): # overriding the dunder methods
    return self.parts[index]
  
  def __call__(self, message): # overriding the dunder methods
    return f'This is object calling with message {message}'

car = Car(1999, [1, 2, 3, 4, 5])
print(len(car)) # 5
print(car[2]) # 3
print(car('Hi there!!!')) # 'This is object calling with message Hi there!!!'
