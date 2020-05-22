# Logical operators

a = 12
b = 20
c = 33
is_valid = True

if (a >= b):
  print('a greater than or equal b')

if (b >= a):
  print('b greater than or equal a')

if (a >= b and c <= a):
  print('and')

if (a >= b or c <= a):
  print('or')

if (a != b and not is_valid):
  print('not')
