# enumerate object
# it returns an object and accepts an iterable

for index, value in enumerate('Hello'):
  print(index, value) # 0, H  1, e ... so on

for index, value in enumerate([1, 2, 3, 4, 5]):
  print(index, value) # 0, 1  1, 2 ... so on
