# Generator (functions which can yield items on the runtime)

def gen_even_sequence(limit):
  for i in range(limit):
    if i % 2 == 0:
      yield i

def even_seq(limit):
  for i in gen_even_sequence(limit):
    print(i)

even_seq(10)
# 0
# 2
# 4
# 6
# 8

# performance test of generators
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
def even_seq_using_generator(limit):
  print('Using generator')
  for i in gen_even_sequence(limit):
    i + i

@performance
def even_seq_using_list(limit):
  print('Using list')
  for i in list(range(limit)):
    if i % 2 == 0:
      i + i

even_seq_using_generator(100000000) # this will take less time than list
even_seq_using_list(100000000) # going to take more time using list approach
