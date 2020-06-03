# Raise error

def divide(num1, num2):
  try:
    if (num2 == 0):
      raise ZeroDivisionError('Denominator is zero')
    return num1 / num2
  except TypeError:
    print('Please enter valid number')
  else:
    print('Successfully executed request')
  
print(divide(1, 0)) # ZeroDivisionError: Denominator is zero
