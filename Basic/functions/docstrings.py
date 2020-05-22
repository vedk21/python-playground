# docstrings
# these are function info attached to the function definition

def get_total_score(scores = []):
  '''
  Accepts scores as an list, default is empty list
  Returns total score
  '''
  return sum(scores)

get_total_score([87, 23, 34])

help(get_total_score) # prints the doc info for this function

print(get_total_score.__doc__) # prints docstring for given function

