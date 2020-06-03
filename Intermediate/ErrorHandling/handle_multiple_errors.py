# Handling multiple types of errors

def divide(num1, num2):
  try:
    return num1 / num2
  except (TypeError, ZeroDivisionError):
    print('Some error has been thrown')
  
divide(1, '1') # 'Some error has been thrown'
divide(1, 0) # 'Some error has been thrown'

# create alias of error object
def divide2(num1, num2):
  try:
    return num1 / num2
  except (TypeError, ZeroDivisionError) as err:
    print(err)

divide2(1, '1') # unsupported operand type(s) for /: 'int' and 'str'
divide2(1, 0) # division by zero
