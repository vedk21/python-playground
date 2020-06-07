# Debugging in python using pdb

from pdb import set_trace

def divide(num1, num2):
  set_trace()
  return num1 / num2

print(divide(1, 'iuiu'))

# by using set_trace() function we can enter pdb interactive console to debug the code
# there are various commands we can use inside interactive console
# a -> print out all arguments
# next -> go to next line
# continue -> continue the code execution
# variable names -> print out variables values
# list -> list out the complete code with current line marker
# exit -> exiting out of console
