# There is another way to open file without closing file manually

import os

# get current directory path
cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(f'{cwd}/test_file.txt', mode = 'r') as test_file:
  print(test_file.readlines())

# mode is an optional parameter to open, default value is read file
# r -> read only
# w -> write only (also creates a file if doesn't exists)
# r+ -> read and write
# a -> appends to the file (also creates a file if doesn't exists)

# In 'w' write mode, it overwrites the complete file with given data
# In 'a' append mode, it appends the given data at the end of file content
# In 'r+' read write mode, it reads the file and then write the given content

with open(f'{cwd}/test_file.txt', mode = 'r+') as test_file:
  text = test_file.write('add w') # it replaces the given characters with existing file characters, and keeps rest other text as it is
  print(text) # prints number of characters written to file

with open(f'{cwd}/test_file.txt', mode = 'a') as test_file:
  text = test_file.write('append text') # it apppends the given characters at the end of file
  print(text) # prints number of characters written to file

with open(f'{cwd}/test_file.txt', mode = 'w') as test_file:
  text = test_file.write('overwrite text') # it overwrites the given characters to the complete file content
  print(text) # prints number of characters written to file

# There is a standard library available for cross platform file operations called 'pathlib'
