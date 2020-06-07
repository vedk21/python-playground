# File error handling

import os

# get current directory path
cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

try:
  with open(f'{cwd}/test1_file.txt', mode = 'r') as test_file:
    print(test_file.readlines())
except FileNotFoundError:
  print('File doesn\'t exists, please check for file path as well')
