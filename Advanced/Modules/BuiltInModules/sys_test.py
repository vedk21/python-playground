from sys import argv

try:
  first_argument = argv[1]
  second_argument = argv[2]
  print(first_argument, second_argument)
except IndexError:
  print('Please enter valid command line arguments')
