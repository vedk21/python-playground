# Multiple inheritace

class Mustang:
  def drive(self):
    print('Driving mustang')

class Camry:
  def drive(self):
    print('Driving camry')

class HybridCar(Mustang, Camry):
  def hybrid(self):
    print('this is hybrid car')

hybrid_car = HybridCar()
hybrid_car.drive() # 'Driving mustang'

# Method resolution order (MRO)
class A:
  num = 10

  def abc(self):
    print('A abc')

class B:
  num = 5

  def abc(self):
    print('B abc')

class C(B, A):
  pass

obj1 = C()
print(obj1.num) # 5
obj1.abc() # 'B abc'

# This is because python uses method resolution order of left -> right
# Hence in above case class B methods and properties will take more priority over class A
