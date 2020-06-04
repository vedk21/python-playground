# How for loop work under the hood

def my_loop(iterable):
  iterator = iter(iterable) # creates iterator from an iterable

  while True:
    try:
      print(next(iterator)) # on calling next on iterator it yields next value
    except StopIteration:
      break

my_loop([1, 2, 3, 4, 5])
# 1
# 2
# 3
# 4
# 5


