# Functions are objects in python, means they can be passed as an argument to another function or can be returned from a function as well

# Function passed as an argument
def do_something():
  print('doing...')

def display(func):
  print('calling another function')
  func()

display(do_something)
# calling another function
# doing...

# Function returned from another function
def driving():
  print('driving...')

def drive():
  return driving

driving_handler = drive()
driving_handler() # driving...
