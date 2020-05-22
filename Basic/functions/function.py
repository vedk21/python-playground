# Function

# function definition
def say_hi():
  print('Hi!')
# call function
say_hi()

# function parameters and arguments
# parameters
def greet(name, message):
  print(f'Hey {name}, {message}')
# arguments
greet('Mark', 'How are you?') # 'Hey Mark, How are you?'

# keyword arguments
greet(message='Who are you?', name='Parker') # 'Hey Parker, Who are you?'

# default paramenters
def print_message(message='default message'):
  print(message)

print_message('please read this message') # 'please read this message'
print_message() # 'default message'

#return statement
def get_sum(a, b):
  return a + b

print(get_sum(10, 5)) # 15
