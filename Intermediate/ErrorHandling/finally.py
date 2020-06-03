# Finally block

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
    finally:
      print('This will execute every time, success or failed')

calculate()

# finally block will execute no matter whether there is error thrown or not
