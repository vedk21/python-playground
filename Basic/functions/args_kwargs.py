# multiple arguments and key-word arguments

def display_param(*args, **kwargs):
  print(args) # it is a tuple of arguments
  print(kwargs) # it is a dictionary of key-word arguments

display_param(1, 2, 3, 4, name = 'simon', age = 34)
# (1, 2, 3, 4)
# {'name': 'simon', 'age': 34}

# We can name those *args and **kwargs anything, but it is common practice to use *args and **kwargs.
