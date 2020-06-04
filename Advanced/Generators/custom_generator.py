# Create generator which can be used with for loop

class EvenGenerator:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __iter__(self):
    return self

  def __next__(self):
    if self.first < self.last:
      if self.first % 2 == 0:
        num = self.first
        self.first += 2
        return num
    raise StopIteration

def run():
  for i in EvenGenerator(0, 10):
    print(i)

run()
