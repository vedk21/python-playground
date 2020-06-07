# File basic open, read and close actions

import os

# get current directory path
cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# open the file
test_file = open(f'{cwd}/test_file.txt')

# read
print(test_file.readline()) # reads the current cursor line
print(test_file.readlines()) # reads files and returns all the lines as list of strings
print(test_file.read()) # reads the complete file

# close the file
test_file.close()
