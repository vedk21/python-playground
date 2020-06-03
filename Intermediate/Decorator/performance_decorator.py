# Example decorator

from time import time

def performance(func):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'It took about {t2 - t1} s')
    return result
  return wrapper

@performance
def loop_through():
  for i in range(100000000):
    i * 5

loop_through()
