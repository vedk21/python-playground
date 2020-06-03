# Error handling in python

def calculate():
  while True:
    try:
      age = int(input('Please enter your age: '))
      100/age
    except ValueError:
      print('Please enter valid number')
    except ZeroDivisionError:
      print('Please enter positive number greater than zero')
    else:
      print('Thank you')
      break

calculate()

# else block is executed only if try executes successfully without error
