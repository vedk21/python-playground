# Decorator

# Without parameters
def my_decorator(func):
  def wrapper():
    print('Enhancing...')
    func()
  return wrapper

@my_decorator
def hello():
  print('Hello...')

hello()
# Enhancing...
# Hello...


# With parameters
def my_decorator2(func):
  def wrapper(*args, **kwargs):
    print('Enhancing...')
    func(*args, **kwargs)
  return wrapper

@my_decorator2
def greet(greeting, emoji = ':)'):
  print(greeting, emoji)

greet('Hey')
# Enhancing...
# Hey :)
